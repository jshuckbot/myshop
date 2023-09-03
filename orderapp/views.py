from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cartapp.cart import Cart
from orderapp import models as orderapp_models
from orderapp.forms import OrderCreateForm
from orderapp.tasks import order_created


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
            order_created.delay(order.id)
            request.session["order_id"] = order.id
            return redirect(reverse("paymentapp:process"))
    else:
        form = OrderCreateForm()
    return render(request, "orderapp/order/create.html", {"cart": cart, "form": form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(orderapp_models.Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})
