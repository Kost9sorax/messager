import json
from django.template.defaultfilters import lower

from api_service.models import Messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .producer import producer


@receiver(post_save, sender=Messages, dispatch_uid="update_stock_count")
def update_stock(sender, instance, created, **kwargs):
    if created:
        data = {
            'id': instance.id,
            'message': lower(instance.message),
            'token': instance.token
        }
        producer.send('Messages', json.dumps(data).encode('utf-8'))
        producer.flush()
