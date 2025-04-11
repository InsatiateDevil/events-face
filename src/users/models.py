from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Определение модели пользователя
    """
    username = models.CharField(verbose_name="Логин", max_length=100, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
