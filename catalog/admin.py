from django.contrib import admin

from catalog.models import Category, Contacts, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения категорий в админке."""

    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения продуктов в админке."""

    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения контактной информации в админке."""

    list_display = ("address", "phone", "email")
