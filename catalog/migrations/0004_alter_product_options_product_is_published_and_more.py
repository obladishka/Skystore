# Generated by Django 5.1.2 on 2024-12-14 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_contacts"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [("can_unpublish_product", "может отменять публикацию продукта")],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="статус публикации"),
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
    ]
