import pickle

from django.utils.decorators import method_decorator

from tesla.common import auth_user
from tesla.user.models import User


class Memento:
    def __init__(self, state):
        self.state = pickle.dumps(state)

    def get(self):
        return pickle.loads(self.state)


class Originator:
    def __init__(self, current_user):
        self.current_user = current_user

    def create_memento(self) -> Memento:
        return Memento(self.current_user)

    def restore(self, m: Memento):
        self.current_user = m.get()


class Con_Table_Module_User:
    snapshot = None

    @method_decorator(auth_user)
    def auth_user(self, login, password):
        user_exist = User.objects.filter(login=login, password=password).exists()
        if user_exist:
            return True
        else:
            return False

    @classmethod
    def make_snapshot(cls, request):
        orig = Originator(request.user)
        snapshot = orig.create_memento()
        cls.snapshot = snapshot

    @classmethod
    def load_snapshot(cls):
        orig = Originator(None)
        orig.restore(cls.snapshot)
        return orig.current_user

