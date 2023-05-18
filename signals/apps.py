from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'

    def ready(self):
        from . import auth_signals, model_signals, req_resp_signals, custom_signals
        return super().ready()
