import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для добавления или редактирования товара."""

    BANNED_WORDS = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")
    ALLOWED_EXTENSIONS = ("jpeg", "png")
    MAX_UPLOAD_SIZE = 5242880

    image = forms.ImageField(widget=forms.FileInput, required=False, validators=[
        FileExtensionValidator(ALLOWED_EXTENSIONS, message="Выберите файл в формате jpeg или png")])

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control mb-3 mt-1", "placeholder": "Введите название товара", "required": True}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control mb-3 mt-1", "placeholder": "Добавьте описание товара"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control mb-5 mt-1", "placeholder": "Загрузите изображение товара"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-select mb-5 my-1"})
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control mb-3 mt-1",
                "placeholder": "Укажите цену товара с копейками",
                "required": True,
                "step": "0.01",
            }
        )

    def clean_name(self):
        """Метод для проверки отсутствия запрещенных слов в названии товара."""
        name = self.cleaned_data.get("name")
        if any(re.search(word, name, flags=re.IGNORECASE) for word in self.BANNED_WORDS):
            raise ValidationError(
                f"В названии содержится запрещенное слово. Список запрещенных слов: {', '.join(self.BANNED_WORDS)}"
            )
        return name

    def clean_description(self):
        """Метод для проверки отсутствия запрещенных слов в описании товара."""
        description = self.cleaned_data.get("description")
        if any(re.search(word, description, flags=re.IGNORECASE) for word in self.BANNED_WORDS):
            raise ValidationError(
                f"В описании содержится запрещенное слово. Список запрещенных слов: {', '.join(self.BANNED_WORDS)}"
            )
        return description

    def clean_price(self):
        """Метод для проверки цены товара."""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price

    def clean_image(self):
        """Метод для проверки изображения товара."""
        image = self.cleaned_data.get("image")
        if image.size > self.MAX_UPLOAD_SIZE:
            raise ValidationError("Размер файла не может превышать 5МВ.")
        return image
