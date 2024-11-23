from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text", "preview"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control mb-3 mt-1", "placeholder": "Введите заголовок статьи", "required": True}
            ),
            "preview": forms.FileInput(attrs={"class": "form-control mb-3 mt-1"}),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 mt-1",
                    "placeholder": "Добавьте содержание статьи",
                    "required": True,
                }
            ),
        }
