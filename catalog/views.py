from django.shortcuts import render


def home(request):
    """Функция для отображения домашней страницы."""
    return render(request, "catalog/home.html")


def contacts(request):
    """Функция для отображения страницы контактов и обработки POST-запросов."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        context = {"name": name}
        return render(request, "catalog/message.html", context)
    return render(request, "catalog/contacts.html")
