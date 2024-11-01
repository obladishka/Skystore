from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home1"),
    path('home/', home, name="home2"),
    path('contacts/', contacts, name="contacts"),
]
