import json

from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

from backend.models import Order
from .constants import OrderEvent


def order_to_dict(order):
    return {
        'id': order.id,
        'orderId': order.order_id,
        'cost': order.cost,
        'costInRubles': order.cost_in_rubles,
        'deliveryTime': order.delivery_time,
    }


class OrderConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            'order-event',
            self.channel_name,
        )

    def receive_json(self, content):
        if isinstance(content, str):
            content = json.loads(content)

        event = content['event']
        if event == 'order-sender':
            order_id = content['data']
            async_to_sync(self.channel_layer.group_send)('order-event', {
                'order_id': order_id,
                'type': 'order.sender',
                'event_type': content['event_type'],
            })

    def order_sender(self, event):
        order_id = event['order_id']
        if event['event_type'] == OrderEvent.Deleted.value:
            self.send(text_data=json.dumps({
                'event': 'order-deleted',
                'data': order_id,
            }))
        elif event['event_type'] == OrderEvent.Created.value:
            order = Order.orders.get(id=order_id)
            self.send(text_data=json.dumps({
                'event': 'order-created',
                'data': order_to_dict(order),
            }, default=str))
        elif event['event_type'] == OrderEvent.Updated.value:
            order = Order.orders.get(id=order_id)
            self.send(text_data=json.dumps({
                'event': 'order-updated',
                'data': order_to_dict(order),
            }, default=str))

    def close(self):
        async_to_sync(self.channel_layer.group_discard)(
            'order-event',
            self.channel_name,
        )
