import json
import traceback

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from websocket import create_connection

from ws.constants import OrderEvent
from .models import Order
from .utils import send_notification_about_expiration


@receiver(post_save, sender=Order)
def order_post_save_handler(instance, created, **kwargs):
    if created:
        event = OrderEvent.Created.value
    else:
        event = OrderEvent.Updated.value

    if instance.delivery_time < timezone.now().date():
        try:
            send_notification_about_expiration(instance)
        except Exception:
            traceback.print_exc()

    data = {
        'data': instance.id,
        'event_type': event,
        'event': 'order-sender',
    }
    try:
        ws = create_connection("ws://0.0.0.0:8880/ws")
        ws.send(json.dumps(data))
        ws.close()
    except Exception:
        traceback.print_exc()


@receiver(post_delete, sender=Order)
def order_post_delete_handler(instance, **kwargs):
    data = {
        'data': instance.id,
        'event_type': OrderEvent.Deleted.value,
        'event': 'order-sender',
    }
    try:
        ws = create_connection("ws://0.0.0.0:8880/ws")
        ws.send(json.dumps(data))
        ws.close()
    except Exception:
        traceback.print_exc()
