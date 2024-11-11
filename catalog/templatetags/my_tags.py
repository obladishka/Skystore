from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """Шаблонный фильтр для работы с медиа файлами."""
    if path:
        return f"/media/{path}"
    return "#"
