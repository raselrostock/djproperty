from django.apps import AppConfig


class RealtorsConfig(AppConfig):
    name = 'realtors'

    def ready(self):
        import djproperty.signals
