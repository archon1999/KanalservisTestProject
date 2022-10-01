from rest_framework import viewsets, permissions

from backend.models import Order
from .paginations import FullDataPagination
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.orders.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = FullDataPagination
    serializer_class = OrderSerializer
