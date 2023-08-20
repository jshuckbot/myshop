from django.shortcuts import render

from cartapp.cart import Cart
from orderapp import models as orderapp_models
from orderapp.forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                orderapp_models.OrderItem.objects.create(
                    order=order, product=item["product"], price=item["price"], quantity=item["quantity"]
                )
            cart.clear()
            return render(request, "orderapp/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orderapp/order/create.html", {"form": form})
