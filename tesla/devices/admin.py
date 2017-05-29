from django.contrib.admin import ModelAdmin

from tesla.devices.models import Device
from tesla.dj import cadmin


def worked(obj):
    return "{}".format(obj.job_set.exists())
worked.short_description = "Работал?"


class Form_Devices(ModelAdmin):
    model = Device
    list_display = ('pk', 'name', 'state', worked)
    search_fields = ('name', 'state')
    list_filter = ('state',)


cadmin.register(Device, Form_Devices)
