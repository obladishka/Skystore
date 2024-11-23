from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView

app_name = BlogConfig.name

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
