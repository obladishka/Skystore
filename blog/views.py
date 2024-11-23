from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article
from catalog.models import Category


class ArticleListView(ListView):
    """Класс для отображения главной страницы блога."""

    model = Article
    ordering = "-views_count"

    def get_context_data(self, object_list=None, **kwargs):
        """Метод для расширения передаваемых данных."""
        context = super().get_context_data(**kwargs)
        context["categories"] = [category.name for category in Category.objects.all()]
        context["top"] = context.get("object_list")[0]
        context["articles"] = context.get("object_list")[1:]
        return context
