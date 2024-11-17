from django import forms

from catalog.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control mb-3 mt-1", "placeholder": "Введите название товара", "required": True}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control mb-3 mt-1", "placeholder": "Добавьте описание товара"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control mb-5 mt-1", "placeholder": "Загрузите изображение товара"}
            ),
            "category": forms.Select(attrs={"class": "form-select mb-5 my-1"}),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3 mt-1",
                    "placeholder": "Укажите цену товара с копейками",
                    "required": True,
                    "step": "0.01",
                }
            ),
        }
