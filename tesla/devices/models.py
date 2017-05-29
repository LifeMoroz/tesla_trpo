from django.db import models


class Device(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    state = models.CharField(verbose_name="Состояние", max_length=255, choices=(('Выкл', 'Выкл'), ('Вкл', 'Вкл')), default='Выкл')

    def __str__(self):
        return "{} ({})".format(self.name, self.get_state_display())

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"