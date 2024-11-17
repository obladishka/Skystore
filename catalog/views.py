from django.shortcuts import render

from catalog.models import Category, Contacts, Product


def home(request, page=0):
    """Функция для отображения домашней страницы."""
    products = Product.objects.all().order_by("-created_at")

    for product in products[:5]:
        print(product)

    products_list = list(products)
    products_list.append(None)

    context = {
        "products": products_list[page * 3 : (page + 1) * 3],
        "range": range((len(products)) // 3 + 3 % 2),
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

        context = {"h1": f"{name}, спасибо за Ваше сообщение!", "h3": "Мы обязательно свяжемся с Вами."}
        return render(request, "catalog/message.html", context)

    context = {"contacts": Contacts.objects.all()}
    return render(request, "catalog/contacts.html", context)


def add_product(request):
    """Функция для добавления товаров."""
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = Category.objects.get(name=request.POST.get("category"))
        price = float(request.POST.get("price")) if float(request.POST.get("price")) >= 0 else 0
        image = request.POST.get("image")
        print(request.POST)

        Product.objects.create(name=name, description=description, category=category, price=price, image=image)

        context = {
            "h1": f"Товар {name} успешно добавлен!",
            "h3": "Обновите главную страницу, чтобы увидеть изменения.",
        }
        return render(request, "catalog/message.html", context)

    context = {"categories": Category.objects.all()}
    return render(request, "catalog/add_product_form.html", context)
