import secrets

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.generic import CreateView

from users.forms import UserAuthenticationForm, UserForm
from users.models import User


class RegisterView(CreateView):

    model = User
    form_class = UserForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        host = self.request.get_host()
        self.send_verification_email(user, host)

        context = {
            "h1": "Спасибо за выбор SkyStore!",
            "h3": "Для завершения регистрации подтвердите свой Email, перейдя по ссылке, отправленной на Вашу почту.",
        }
        return render(self.request, "catalog/message.html", context)

    @staticmethod
    def send_verification_email(user, host):
        """Функция для отправки письма для завершения регистрации."""

        context = {
            "url": f"http://{host}/users/user-verification/{user.token}",
        }

        subject = "Добро пожаловать в SkyStore!"
        html_message = render_to_string("registration/welcome_letter.html", context)
        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, None, [user.email], html_message=html_message)


class UserLoginView(LoginView):

    model = User
    form_class = UserAuthenticationForm

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        remember_me = form.cleaned_data["remember_me"]
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)


def user_verification(request, token):
    """Функция для подтверждения почты."""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
