from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'tesla.user'
    verbose_name = "Пользователи"

default_app_config = 'tesla.user.UserConfig'
