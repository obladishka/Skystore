from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactsListViewWithPost, ProductCreateView, ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("detail/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    path("new/", ProductCreateView.as_view(), name="add_product"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
    path("contacts/", ContactsListViewWithPost.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
