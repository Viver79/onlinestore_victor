from django.urls import path
from .views import *
from . import views

urlpatterns = [
     path('', bicycles, name='bicycles'),
     path('bike_single/<int:bike_id>/', bike_single, name='bike_single'),
     path('bicycles_single/<int:type_id>', bicycles_single, name='bicycles_single'),

     path('control_bicycles/', control_bicycles, name='control_bicycles'),
     path('control_bicycles/add_bicycles', ControlAddBicycles.as_view(), name='add_bicycles'),
     path('categories_type/update_bicycles/<int:pk>/', ControlUpdateBicycles.as_view(), name='update_bicycles'),
     path('categories_type/delete_bicycles/<int:pk>/', ControlDeleteBicycles.as_view(), name='delete_bicycles'),
     path('categories_type/', categories_type, name='categories_type'),
     path('categories_brand/', categories_brand, name='categories_brand'),
     path('categories_type/add_type', CategoryAddType.as_view(), name='add_bike_type'),
     path('categories_type/update_type/<int:pk>/', CategoryUpdateType.as_view(), name='update_type'),
     path('categories_type/delete_type/<int:pk>/', CategoryDeleteType.as_view(), name='delete_type'),
     path('categories_brand/add_brand', CategoryAddBrand.as_view(), name='add_bike_brand'),
     path('categories_brand/update_brand/<int:pk>/', CategoryUpdateBrand.as_view(), name='update_bike_brand'),
     path('categories_brand/delete_brand/<int:pk>/', CategoryDeleteBrand.as_view(), name='delete_bike_brand'),

     ]