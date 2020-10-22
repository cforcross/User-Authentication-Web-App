from django.apps import AppConfig


class AuthappConfig(AppConfig):
    name = 'authapp'

    def ready(self):
        from . import signals
