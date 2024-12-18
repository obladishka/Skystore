from catalog.models import Category


class ProductService:
    """Класс для формирования бизнес-логики для работы с продуктами."""

    @staticmethod
    def get_products_by_category(category_id):
        """Метод для получения списка товаров определенной категории."""

        category = Category.objects.get(pk=category_id)
        return category.products.all()
