from django.shortcuts import get_object_or_404, render

from shopapp import models as shopapp_models
from cartapp.forms import CartAddProductForm


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


def product_detail(request, id, slug):
    product = get_object_or_404(shopapp_models.Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shopapp/product/detail.html", {"product": product, 'cart_product_form': cart_product_form})
