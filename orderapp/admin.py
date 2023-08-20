from django.contrib import admin

from orderapp import models as orderapp_models


class OrderItemInline(admin.TabularInline):
    model = orderapp_models.OrderItem
    raw_id_fields = ["product"]


@admin.register(orderapp_models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]