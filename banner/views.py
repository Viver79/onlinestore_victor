from django.shortcuts import render
from bicycles.models import Bike_type


# def banner(request):
#     banner_bike_type = Bike_type.objects.filter(is_visible=True).order_by('categories_bicycles')
#     return render(request, 'container.html', context={'banner_bike_type': banner_bike_type})