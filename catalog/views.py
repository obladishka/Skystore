from django.shortcuts import render

from catalog.models import Product


def home(request):
    """Функция для отображения домашней страницы."""
    products = Product.objects.order_by("-created_at")[:5]

    for product in products:
        print(product)

    context = {"products": products}

    return render(request, "catalog/home.html", context)


def contacts(request):
    """Функция для отображения страницы контактов и обработки POST-запросов."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        context = {"name": name}
        return render(request, "catalog/message.html", context)
    return render(request, "catalog/contacts.html")
