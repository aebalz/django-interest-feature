from apis.tasks.models import Task
from django.dispatch import receiver
from django.db.models.signals import post_init, post_save


@receiver(post_save, sender=Task)
def send_notification(sender, instance, created, **kwargs):
    print(f"{created = }")
    print(f"{instance.__class__} was created")
    # do something sending notification
