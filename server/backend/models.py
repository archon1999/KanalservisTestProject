from django.db import models
from django.contrib.auth.models import AbstractUser
from solo.models import SingletonModel


class Order(models.Model):
    orders = models.Manager()
    order_id = models.IntegerField()
    cost = models.PositiveIntegerField()
    cost_in_rubles = models.FloatField(null=True, blank=True)
    delivery_time = models.DateField(max_length=255)

    class Meta:
        ordering = ['-id']


class User(AbstractUser):
    pass


class RubleExchangeRate(SingletonModel):
    value = models.PositiveIntegerField(default=60)

    class Meta:
        verbose_name = "Курс рубля"
