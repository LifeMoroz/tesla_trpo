from django.apps import AppConfig


class DevicesConfig(AppConfig):
    name = 'tesla.devices'
    verbose_name = "Устройства"

default_app_config = 'tesla.devices.DevicesConfig'
