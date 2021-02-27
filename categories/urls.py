from  django.urls import path
from .views import *

urlpatterns =[
    path('categories', categories, name='categories'),
    path('categories/update/<int:pk>/', CategoriesUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', CategoriesDeleteView.as_view(), name='categories_delete'),
    path('categories/add', CategoriesAddView.as_view(), name='categories_add'),

]