from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
