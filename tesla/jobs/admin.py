from django.contrib.admin import ModelAdmin

from tesla.dj import cadmin
from tesla.jobs.models import Job


# admin.site.register(Job)


class Form_Jobs(ModelAdmin):
    model = Job
    list_display = ('pk', '__str__', 'today', 'month', 'quart', 'half_year', 'year')


cadmin.register(Job, Form_Jobs)
