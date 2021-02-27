from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bicycles.models import ProductBicycles
from .models import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, bike_id):
    cart = Cart(request)
    bike = get_object_or_404(ProductBicycles, id=bike_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(bike=bike,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, bike_id):
    cart = Cart(request)
    bike = get_object_or_404(ProductBicycles, id=bike_id)
    cart.remove(bike)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],
                                                                'update':True})
    return render(request, 'cart.html', {'cart':cart})