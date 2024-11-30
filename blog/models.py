from django.db import models


class Article(models.Model):
    """Таблица статей."""

    title = models.CharField(max_length=150, verbose_name="Заголовок", help_text="Введите заголовок статьи")
    text = models.TextField(verbose_name="Содержание", help_text="Добавьте содержание статьи")
    preview = models.ImageField(
        upload_to="articles/",
        verbose_name="Превью",
        help_text="Загрузите превью статьи",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}: {self.text[:100]}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
