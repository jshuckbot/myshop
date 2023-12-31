from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cartapp/", include("cartapp.urls", namespace="cartapp")),
    path("orderapp/", include("orderapp.urls", namespace="orderapp")),
    path("paymentapp/", include("paymentapp.urls", namespace="paymentapp")),
    path("", include("shopapp.urls", namespace="shopapp")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
