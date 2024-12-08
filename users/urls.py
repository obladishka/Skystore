from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.forms import UserAuthenticationForm
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(form_class=UserAuthenticationForm), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
