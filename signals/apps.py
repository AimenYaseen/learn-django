from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'

    def ready(self):
        from . import auth_signals
        return super().ready()
