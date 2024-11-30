from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения статей в админке."""

    list_display = ("id", "title", "text")
    list_filter = ("is_published", "created_at", "views_count")
    search_fields = ("title", "text")
