from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['bike']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'created', 'updated', 'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemInline]