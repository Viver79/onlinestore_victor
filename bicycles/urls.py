from django.urls import path
from .views import *
from . import views

urlpatterns = [
     path('', bicycles, name='bicycles'),
#     path('<int:bike_id>/', bike_single, name='bike_single'),
     path('bike_single/<int:bike_id>/', bike_single, name='bike_single'),
     path('bicycles_single/<int:type_id>', bicycles_single, name='bicycles_single'),

     path('categories_bike/', categories_bike, name='categories_bike'),
     path('categories_bike/update_type/<int:pk>/', CategoryUpdateBike.as_view(), name='update_bike_type'),
     path('categories_bike/delete_type/<int:pk>/', CategoryDeleteBike.as_view(), name='delete_bike_type'),
     path('categories_bike/add_type', CategoryAddBike.as_view(), name='add_bike_type'),
     path('categories_bike/add_brand', CategoryAddBrand.as_view(), name='add_bike_brand'),
     path('categories_bike/update_brand/<int:pk>/', CategoryUpdateBrand.as_view(), name='update_bike_brand'),
     path('categories_bike/delete_brand/<int:pk>/', CategoryDeleteBrand.as_view(), name='delete_bike_brand'),


     ]