from django.apps import AppConfig


class NewDoorConfig(AppConfig):
    name = 'new_door'
    def ready(self):
        import new_door.signals