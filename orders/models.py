from django.db import models
from bicycles.models import ProductBicycles

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    bike = models.ForeignKey(ProductBicycles, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity