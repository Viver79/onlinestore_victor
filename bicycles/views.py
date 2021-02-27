from django.shortcuts import render, get_object_or_404
from bicycles.models import ProductBicycles, Bike_type
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

# def bike_single(request, bike_id):
#     bike = get_object_or_404(ProductBicycles, id=bike_id, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'bike_single.html', {'bike':bike, 'cart_product_form': cart_product_form})




# def add_bike_type(request):
#     if request.method == 'POST':
#         form = Bike_typeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return
#     else:
#         form = Bike_typeForm()
#         return render(request, 'add_bike_type.html', context={'form':form})

def categories_bike(request):
    items = Bike_type.objects.all().order_by('categories_bicycles')
    brand = Bike_brand.objects.all().order_by('categories_bicycles')
    return render(request, 'categories_bike.html', context={'items': items,
                                                            'brand':brand})

class CategoryAddBike(SuccessMessageMixin, CreateView):
    model = Bike_type
    form_class = Bike_typeForm
    template_name = 'add_bike_type.html'
    success_url = reverse_lazy('bicycles:categories_bike')
    success_message = 'Категорія успешно создана!'

class CategoryUpdateBike(SuccessMessageMixin, UpdateView):
    model = Bike_type
    form_class = Bike_typeForm, Bike_brandForm
    template_name = 'update_bike_type.html'
    success_url = reverse_lazy('bicycles:categories_bike')
    success_message = 'Категорія успішно відкоригована!'

class CategoryDeleteBike(DeleteView):
    model = Bike_type
    success_url = reverse_lazy('bicycles:categories_bike')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категорія успішно видалена!')
        return self.post(request, *args, **kwargs)

class CategoryAddBrand(SuccessMessageMixin, CreateView):
    model = Bike_brand
    form_class = Bike_brandForm
    template_name = 'add_bike_brand.html'
    success_url = reverse_lazy('bicycles:categories_bike')
    success_message = 'Производитель (бренд) успешно добавлен!'

class CategoryUpdateBrand(SuccessMessageMixin, UpdateView):
    model = Bike_brand
    form_class = Bike_brandForm
    template_name = 'update_bike_brand.html'
    success_url = reverse_lazy('bicycles:categories_bike')
    success_message = 'Категорія успішно відкоригована!'

class CategoryDeleteBrand(DeleteView):
    model = Bike_brand
    success_url = reverse_lazy('bicycles:categories_bike')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)
