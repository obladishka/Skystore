from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import add_product, contacts, home, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("home/<int:page>/", home, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:id>/", product_detail, name="product_detail"),
    path("products/new/", add_product, name="add_product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
