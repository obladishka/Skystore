from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")

    def __init__(self, *args, **kwargs):
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
