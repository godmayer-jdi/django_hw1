from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="Добавьте своё фото")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=50, verbose_name="Страна", blank=True, null=True, help_text="Введите название страны")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return self.email
