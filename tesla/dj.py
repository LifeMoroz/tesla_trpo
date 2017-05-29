from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from tesla.user.views import Con_Table_Module_User


class CustomAdmin(AdminSite):

    def has_permission(self, request):
        return super().has_permission(request)

    @staticmethod
    def make_snapshot(request):
        Con_Table_Module_User.make_snapshot(request)
        return HttpResponseRedirect("/admin/")

    @staticmethod
    def load_snapshot(request):
        login(request, Con_Table_Module_User.load_snapshot())
        return HttpResponseRedirect("/admin/")

    def get_urls(self):
        urls = super(CustomAdmin, self).get_urls()
        my_urls = [
            url(r'^add_snapshot/$', self.make_snapshot),
            url(r'^load_snapshot/$', self.load_snapshot),
        ]
        return my_urls + urls

cadmin = CustomAdmin()
pass
