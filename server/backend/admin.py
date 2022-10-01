from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Order, RubleExchangeRate


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'cost', 'cost_in_rubles',
                    'delivery_time']


@admin.register(RubleExchangeRate)
class RubleExchangeRateAdmin(SingletonModelAdmin):
    pass
