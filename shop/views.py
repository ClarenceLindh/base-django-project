from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from .models import Shop
from .serializers import ShopSerializer


class ShopDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"

class ShopListView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
