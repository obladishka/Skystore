from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Article


class ArticleListView(ListView):
    """Класс для отображения главной страницы блога."""

    model = Article
    ordering = "-views_count"

    def get_context_data(self, object_list=None, **kwargs):
        """Метод для расширения передаваемых данных."""
        context = super().get_context_data(**kwargs)
        context["top"] = context.get("object_list")[0]
        context["articles"] = context.get("object_list")[1:]
        return context


class ArticleDetailView(DetailView):
    """Класс для отображения полного текста статьи."""

    model = Article
