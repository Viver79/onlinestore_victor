from django.contrib import admin
from .models import Bike_brand, Bike_type, Bike_size, ProductBicycles

# Register your models here.
class ProductBicyclesAdmin(admin.ModelAdmin):
    list_display = ('bike_type', 'titel', 'titel_model', 'bike_brand', 'price', 'available')
    list_display_links = ('bike_type', 'titel', 'titel_model', 'bike_brand', 'price', 'available')
    search_fields = ('bike_type', 'titel', 'titel_model', 'bike_brand', 'price', 'available')

class Bike_typeAdmin(admin.ModelAdmin):
    list_display = ('title', 'categories_bicycles', 'is_visible')
    list_display_links = ('title', 'categories_bicycles', 'is_visible')
    search_fields = ('title', 'categories_bicycles', 'is_visible')

admin.site.register(Bike_size)
admin.site.register(Bike_brand)
admin.site.register(Bike_type, Bike_typeAdmin)
admin.site.register(ProductBicycles, ProductBicyclesAdmin)