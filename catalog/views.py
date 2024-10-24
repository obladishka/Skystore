from django.shortcuts import render


def home(request):
    """Функция для отображения домашней страницы."""
    return render(request, "catalog/home.html")


def contacts(request):
    """Функция для отображения страницы контактов."""
    return render(request, "catalog/contacts.html")
