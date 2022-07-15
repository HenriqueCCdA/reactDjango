from django.views import View
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListSerializer, ItemSerializer
from .models import Item, List


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes =  [permissions.IsAuthenticated]
