from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Permission
from django.http import HttpResponseRedirect


def add_user_decorator(func):
    def wrap(login, password):
        user = User.objects.create_user(login, password=password)
        permissions = User.objects.get(id=2).user_permissions.all()
        user.is_staff = 1
        user.save()
        user.user_permissions.add(*permissions)
        return func(login, password)
    return wrap


def auth_user(func):
    def wrap(login, password):
        user = authenticate(login=login, password=password)
        if not user or not user.is_authenticated:
            return HttpResponseRedirect("/admin/")
        return func(login, password)
    return wrap


@add_user_decorator
def auth(login, password):
    return True
