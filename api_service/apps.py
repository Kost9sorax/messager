from django.apps import AppConfig


class ApiServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_service'

    def ready(self):
        import api_service.signals
