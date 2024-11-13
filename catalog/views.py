from django.shortcuts import render

from catalog.models import Contacts, Product


def home(request, page=0):
    """Функция для отображения домашней страницы."""
    products = Product.objects.order_by("-created_at")

    for product in products[:5]:
        print(product)

    context = {
        "products": products[
            page if page == 0 else page + 2 : page + 3 if page + 3 <= len(products) else len(products)
        ],
        "last_product": list(products)[-1],
        "range": range(len(products) // 3 + 1),
    }

    return render(request, "catalog/home.html", context)


def product_detail(request, id):
    """Функция для отображения страницы конкретного товара."""
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)


def contacts(request):
    """Функция для отображения страницы контактов и обработки POST-запросов."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        context = {"name": name}
        return render(request, "catalog/message.html", context)

    context = {"contacts": Contacts.objects.all()}
    return render(request, "catalog/contacts.html", context)
