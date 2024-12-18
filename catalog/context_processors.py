from catalog.models import Category


def add_menu_context(request):
    """Функция для вывода категорий в меню."""

    return {"categories": Category.objects.all()}
