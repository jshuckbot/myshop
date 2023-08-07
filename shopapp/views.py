from django.shortcuts import get_object_or_404, render

from shopapp import models as shopapp_models


def product_list(request, category_slug=None):
    category = None
    categories = shopapp_models.Category.objects.all()
    products = shopapp_models.Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(shopapp_models.Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request, "shopapp/product/list.html", {"category": category, "categories": categories, "products": products}
    )
