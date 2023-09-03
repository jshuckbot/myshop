from io import BytesIO

import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from orderapp import models as orderapp_models


@shared_task
def payment_completed(order_id):
    """Задание по отправке уведомлений по электронной почте при успешной оплате заказа"""
    order = orderapp_models.Order.objects.get(id=order_id)
    subject = f"My Shop - Invoice no. {order.id}"
    message = "Please, find attached the invoice for your recent purchase"
    email = EmailMessage(subject, message, "admin@myshop.com", [order.email])

    html = render_to_string("orderapp/order/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")
    email.send()
