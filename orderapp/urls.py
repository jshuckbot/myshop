from django.urls import path

from orderapp import views

app_name = "orderapp"

urlpatterns = [path("create/", views.order_create, name="order_create")]
