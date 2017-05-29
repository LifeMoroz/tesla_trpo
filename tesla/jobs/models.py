from django.db import models

from tesla.devices.models import Device


class Job(models.Model):
    device = models.ForeignKey(Device)
    today = models.IntegerField(verbose_name="Работа за сегодня")
    month = models.IntegerField(verbose_name="Работа за месяц")
    quart = models.IntegerField(verbose_name="Работа за квартал")
    half_year = models.IntegerField(verbose_name="Работа за полгода")
    year = models.IntegerField(verbose_name="Работа за год")

    def __str__(self):
        return "Работа {}".format(self.device)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"