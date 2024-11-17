from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsListViewWithPost, ProductCreateView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("new/", ProductCreateView.as_view(), name="add_product"),
    path("contacts/", ContactsListViewWithPost.as_view(), name="contacts"),
    # path("home/<int:page>/", home, name="index"),
    # path("contacts/", contacts, name="contacts"),
    # path("products/<int:id>/", product_detail, name="product_detail"),
    # path("products/new/", add_product, name="add_product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
