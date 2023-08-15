from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from cartapp.cart import Cart
from cartapp.forms import CartAddProductForm
from shopapp import models as shopapp_models


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(shopapp_models.Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], override_quantity=cd["override_quantity"])
    return redirect("cartapp:cart_detail")
