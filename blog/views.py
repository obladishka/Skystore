from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    """Класс для отображения главной страницы блога."""

    model = Article

    def get_context_data(self, object_list=None, **kwargs):
        """Метод для расширения передаваемых данных."""
        context = super().get_context_data(**kwargs)
        context["top"] = context.get("object_list")[0]
        context["articles"] = context.get("object_list")[1:]
        return context

    def get_queryset(self):
        """Метод для фильтрации только опубликованных статей."""
        return Article.objects.filter(is_published=True).order_by("-views_count")


class ArticleDetailView(DetailView):
    """Класс для отображения полного текста статьи."""

    model = Article

    def get_object(self, queryset=None):
        """Метод для увеличения количества просмотров статьи."""
        self.object = super().get_object(queryset)
        self.object.views_count += 1

        if self.object.views_count == 100:
            send_congratulations(self.request, self.object)

        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    """Класс для создания статей."""

    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    """Класс для создания статей."""

    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        """Метод для перевода клиента на измененную статью после завершения редактирования."""
        success_url = reverse("blog:article_detail", args=[self.kwargs.get("pk")])
        return success_url


class ArticleDeleteView(DeleteView):
    """Класс для создания статей."""

    model = Article
    success_url = reverse_lazy("blog:article_list")


def send_congratulations(request, article):
    """Функция для отправки поздравления."""

    context = {
        "article": article,
    }

    subject = "Поздравляем!"
    html_message = render_to_string("blog/congratulations.html", context)
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, None, ["nasty-goldyba@yandex.ru"], html_message=html_message)
