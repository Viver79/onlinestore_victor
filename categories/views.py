from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView

# Create your views here.

# def categories(request):
#     item = Categories.objects.all().order_by('categories_bike')
#     return render(request, 'categories.html', context={'item':item})

class CategoriesUpdateView(SuccessMessageMixin, UpdateView):
    pass

class CategoriesAddView(SuccessMessageMixin, CreateView):
    pass

class CategoriesDeleteView(SuccessMessageMixin, DeleteView):
    pass
