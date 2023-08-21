from celery import shared_task
from django.core.mail import send_mail

from orderapp import models as orderapp_models


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведдомления по электронной почте при успешном создании
    """
    order = orderapp_models.Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name}, \n\n" f"You have successfully placed an order." f"Your order ID is {order.id}"
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
