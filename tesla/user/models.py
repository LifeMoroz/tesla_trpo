from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="Логин", max_length=255)
    password = models.CharField(verbose_name="Пароль", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
