from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Contacts, Product


class ProductListView(ListView):
    """Класс для отображения домашней страницы."""

    model = Product
    template_name = "catalog/product_list.html"
    paginate_by = 3
    context_object_name = "products"
    ordering = "-created_at"

    def get_queryset(self):
        """Метод для изменения полученных данных."""
        queryset = list(super().get_queryset())
        queryset.append(None)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс для отображения страницы конкретного товара."""

    model = Product


class ContactsListViewWithPost(ListView):
    """Класс для отображения страницы контактов и обработки POST-запросов."""

    model = Contacts
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"

    def post(self, request, *args, **kwargs):
        """Метод для обработки POST-запросов."""
        name = self.request.POST.get("name")
        context = {"h1": f"{name}, спасибо за Ваше сообщение!", "h3": "Мы обязательно свяжемся с Вами."}
        return render(request, "catalog/message.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для добавления товаров."""

    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        """Метод для обработки POST-запросов."""
        form.save()
        name = self.request.POST.get("name")
        context = {
            "h1": f"Товар {name} успешно добавлен!",
            "h3": "Обновите главную страницу, чтобы увидеть изменения.",
        }
        return render(self.request, "catalog/message.html", context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для изменения товара."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления товара."""

    model = Product
    success_url = reverse_lazy("catalog:product_list")
