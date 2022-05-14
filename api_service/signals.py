from .models import Messages
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Messages, dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
    current = instance
    previous = Messages.objects.get(id=instance.id)
