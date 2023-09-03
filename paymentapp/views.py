from decimal import Decimal

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, reverse

from orderapp import models as orderapp_models

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(orderapp_models.Order, id=order_id)
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("paymentapp:completed"))
        cancel_url = request.build_absolute_uri(reverse("paymentapp:canceled"))

        # данные сеанса оформления платежа
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }

        for item in order.items.all():
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(item.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {
                            "name": item.product.name,
                        },
                    },
                    "quantity": item.quantity,
                }
            )

        # Создать сеанс оформления платежа Stripe
        session = stripe.checkout.Session.create(**session_data)

        # Перенаправить к платежной форме Stripe
        return redirect(session.url, code=303)
    else:
        return render(request, "paymentapp/process.html", locals())


def payment_completed(request):
    return render(request, "paymentapp/completed.html")


def payment_canceled(request):
    return render(request, "paymentapp/canceled.html")
