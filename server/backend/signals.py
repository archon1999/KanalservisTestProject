import json

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from websocket import create_connection

from ws.constants import OrderEvent
from .models import Order


@receiver(post_save, sender=Order)
def order_post_save_handler(instance, created, **kwargs):
    if created:
        event = OrderEvent.Created.value
    else:
        event = OrderEvent.Updated.value

    data = {
        'data': instance.id,
        'event_type': event,
        'event': 'order-sender',
    }
    ws = create_connection("ws://0.0.0.0:8880/ws")
    ws.send(json.dumps(data))
    ws.close()


@receiver(post_delete, sender=Order)
def order_post_delete_handler(instance, **kwargs):
    data = {
        'data': instance.id,
        'event_type': OrderEvent.Deleted.value,
        'event': 'order-sender',
    }
    ws = create_connection("ws://0.0.0.0:8880/ws")
    ws.send(json.dumps(data))
    ws.close()
