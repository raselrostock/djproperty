from django.apps import AppConfig


class ListingsConfig(AppConfig):
    name = 'listings'

    def ready(self):
        import djproperty.signals
