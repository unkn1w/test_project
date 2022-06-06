from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass

