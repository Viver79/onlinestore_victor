from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from braces.views import GroupRequiredMixin
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from cart.forms import CartAddProductForm
from .forms import *


def bicycles(request):
    bike_type = Bike_type.objects.filter(is_visible=True).order_by('categories_bicycles')
    for item in bike_type:
        item.bicycles = ProductBicycles.objects.filter(bike_type=item.id)
    return render(request, 'bicycles.html', context={'bike_type': bike_type,})


def bike_single(request, bike_id):
    bike = ProductBicycles.objects.get(pk=bike_id)
    cart_product_form = CartAddProductForm()# Форма добовления в корзину
    return render(request, 'bike_single.html', {'bike': bike,
                                                'cart_product_form': cart_product_form})

def bicycles_single(request, type_id):
    bicycles_single_type = Bike_type.objects.get(pk=type_id)
    bikes = ProductBicycles.objects.all()
    current_bike = ProductBicycles.objects.filter(bike_type=bicycles_single_type)
    return render(request, 'bicycles_single.html', context={'current_bike': current_bike,
                                                            'bicycles_single_type': bicycles_single_type,
                                                            'bikes':bikes})


def is_member(user):
    return user.groups.filter(name='manager').exists() or \
           user.is_staff

@login_required(login_url='/login/')
@user_passes_test(is_member)
def control_bicycles(request):
    items_bicycles = ProductBicycles.objects.all().order_by('titel_model')
    return render(request, 'control_bicycles.html', context={'items_bicycles': items_bicycles})


@login_required(login_url='/login/')
@user_passes_test(is_member)
def categories_type(request):
    items_type = Bike_type.objects.all().order_by('categories_bicycles')
    return render(request, 'categories_type.html', context={'items_type': items_type})


@login_required(login_url='/login/')
@user_passes_test(is_member)
def categories_brand(request):
    brand = Bike_brand.objects.all().order_by('categories_bicycles')
    return render(request, 'categories_brand.html', context={'brand':brand})


class ControlAddBicycles(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = ProductBicycles
    form_class = ProductBicyclesForm
    template_name = 'add_bicycles.html'
    success_url = reverse_lazy('bicycles:control_bicycles')
    success_message = 'Велосипед успешно создан!'


class ControlUpdateBicycles(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = ProductBicycles
    form_class = ProductBicyclesForm
    template_name = 'update_bicycles.html'
    success_url = reverse_lazy('bicycles:control_bicycles')
    success_message = 'Велосипед успешно отредактирован!'


class ControlDeleteBicycles(LoginRequiredMixin, GroupRequiredMixin,  DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = ProductBicycles
    success_url = reverse_lazy('bicycles:control_bicycles')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Велосипед успешно удален!')
        return self.post(request, *args, **kwargs)


class CategoryAddType(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_type
    form_class = Bike_typeForm
    template_name = 'add_bike_type.html'
    success_url = reverse_lazy('bicycles:categories_type')
    success_message = 'Категория успешно создана!'


class CategoryUpdateType(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_type
    form_class = Bike_typeForm
    template_name = 'update_bike_type.html'
    success_url = reverse_lazy('bicycles:categories_type')
    success_message = 'Категория успешно отредактирована!'


class CategoryDeleteType(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_type
    success_url = reverse_lazy('bicycles:categories_type')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)


class CategoryAddBrand(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_brand
    form_class = Bike_brandForm
    template_name = 'add_bike_brand.html'
    success_url = reverse_lazy('bicycles:categories_brand')
    success_message = 'Производитель (бренд) успешно добавлен!'


class CategoryUpdateBrand(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_brand
    form_class = Bike_brandForm
    template_name = 'update_bike_brand.html'
    success_url = reverse_lazy('bicycles:categories_brand')
    success_message = 'Категория успешно отредактирована!'


class CategoryDeleteBrand(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Bike_brand
    success_url = reverse_lazy('bicycles:categories_brand')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)