from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis.tasks'

    def ready(self):
        import apis.tasks.signals
