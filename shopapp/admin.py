from django.contrib import admin

from shopapp import models as shopapp_models


@admin.register(shopapp_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(shopapp_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}
