from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from backend.views import UserViewSet, GroupViewSet
from core.views import ItemViewSet, ListViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet)
router.register(r'item', ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
