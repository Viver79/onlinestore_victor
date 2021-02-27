from django.urls import path
from . import views
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:bike_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:bike_id>/', views.cart_remove, name='cart_remove'),

    ]