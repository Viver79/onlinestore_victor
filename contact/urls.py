from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='contact'),
    path('update/<int:pk>/', update_messages, name='update'),

]