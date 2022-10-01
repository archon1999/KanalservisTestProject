from rest_framework import routers

from .views import OrderViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet)

urlpatterns = router.urls
