from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import COUNTRIES


class UserManager(BaseUserManager):
    """Класс для управления созданием пользователей."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле 'Email' обязательно для заполнения")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Класс для создания пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите свой email")
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Фото",
        help_text="Загрузите фото",
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=30, choices=COUNTRIES, verbose_name="Страна", help_text="Выберите страну", null=True, blank=True
    )
    remember_me = models.BooleanField(default=False, verbose_name="Запомнить меня")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
