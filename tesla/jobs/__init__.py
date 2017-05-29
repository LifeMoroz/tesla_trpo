from django.apps import AppConfig


class JobsConfig(AppConfig):
    name = 'tesla.jobs'
    verbose_name = "Работа"

default_app_config = 'tesla.jobs.JobsConfig'
