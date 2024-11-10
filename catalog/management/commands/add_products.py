from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавляет тестовые категории и продукты в бд, предварительно ее очистив."

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command("loaddata", "categories_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Добавление категорий прошло успешно."))

        call_command("loaddata", "products_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Добавление продуктов прошло успешно."))
