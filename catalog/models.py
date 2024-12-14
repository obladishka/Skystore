from django.db import models

from users.models import User


class Category(models.Model):
    """Таблица категорий товаров."""

    name = models.CharField(
        max_length=150, verbose_name="наименование", help_text="Введите название категории", unique=True
    )
    description = models.TextField(
        verbose_name="описание", help_text="Добавьте описание категории", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    """Таблица товаров."""

    name = models.CharField(max_length=150, verbose_name="наименование", help_text="Введите название товара")
    description = models.TextField(
        verbose_name="описание", help_text="Добавьте описание товара", null=True, blank=True
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="изображение",
        help_text="Загрузите изображение товара",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="категория",
        help_text="Выберите категорию товара",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена за покупку", help_text="Укажите цену товара с копейками"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name="владелец",
        null=True,
        blank=True,
    )
    is_published = models.BooleanField(default=True, verbose_name="опубликован")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}, категория: {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ("can_unpublish_product", "может отменять публикацию продукта"),
        ]


class Contacts(models.Model):
    """Таблица контактной информации."""

    address = models.TextField(verbose_name="адрес", help_text="Введите адрес компании")
    phone = models.CharField(max_length=20, verbose_name="телефон", help_text="Укажите телефон для связи")
    email = models.EmailField()

    def __str__(self):
        return f"{self.phone}, {self.email}, {self.address}"

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"
