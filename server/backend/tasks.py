import datetime
from pathlib import Path

import pygsheets
from django.db.models import F

from .models import Order, RubleExchangeRate
from .utils import get_ruble_exchange_rate


def parse_delivery_time(delivery_time_str):
    d, m, y = map(int, delivery_time_str.split('.'))
    return datetime.date(y, m, d)


def update_data():
    service_file = Path(__file__).parent / 'service_file.json'
    gc = pygsheets.authorize(service_file=service_file)
    sh = gc.open_by_key('1LSNM1-_k-iPJVaNvcDuwM0LMTPj8xjFlbxRe1Jx7BkA')
    wks: pygsheets.Worksheet = sh.sheet1
    orders = []
    for record in wks.get_all_records():
        order_id = record['order_id']
        orders.append(order_id)
        cost = record['cost']
        delivery_time = parse_delivery_time(record['delivery_time'])
        rate = RubleExchangeRate.objects.get()
        if Order.orders.filter(order_id=order_id).exists():
            order = Order.orders.get(order_id=order_id)
            if cost != order.cost or order.delivery_time != delivery_time:
                order.order_id = order_id
                order.delivery_time = delivery_time
                order.cost = cost
                order.cost_in_rubles = cost * rate.value
                order.save()
        else:
            cost_in_rubles = cost * rate.value
            Order.orders.create(
                order_id=order_id,
                cost=cost,
                delivery_time=delivery_time,
                cost_in_rubles=cost_in_rubles,
            )

    Order.orders.exclude(order_id__in=orders).delete()


def update_ruble_exchange_rate():
    rate = RubleExchangeRate.objects.get()
    if (value := get_ruble_exchange_rate()):
        rate.value = value
        rate.save()

    update_order_cost_in_rubles()


def update_order_cost_in_rubles():
    rate = RubleExchangeRate.objects.get()
    Order.orders.all().update(
        cost_in_rubles=F('cost')*rate.value,
    )
