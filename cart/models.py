import json
from django.db import models
from decimal import Decimal
from django.conf import settings
from bicycles.models import ProductBicycles


class Cart(object):

    def __init__(self, request):
        ''' Инициализация объекта корзины.'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Сохраняем пустую корзину
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        '''Проходим по всем товарам в корзине.'''
        bike_ids = self.cart.keys()
        bikes = ProductBicycles.objects.filter(id__in=bike_ids)

        cart = self.cart.copy()
        for bike in bikes:
            cart[str(bike.id)]['bike'] = bike

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''Возвращаем общее количество товара в корзине'''
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, bike, quantity=1, update_quantity=False):
        '''Добавление товара в корзину или обновление его количества'''
        bike_id = str(bike.id)
        if bike_id not in self.cart:
            self.cart[bike_id] = {'quantity': 0,
                                  'price': str(bike.price)}
        if update_quantity:
            self.cart[bike_id]['quantity'] = quantity
        else:
            self.cart[bike_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Помечаем сесию как измененную
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, bike):
        '''Удаление товара из корзины.'''
        bike_id = str(bike.id)
        if bike_id in self.cart:
            del self.cart[bike_id]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        '''Очистка корзины.'''
        del self.session[settings.CART_SESSION_ID]
        self.save()