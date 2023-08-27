from django.urls import path
from .views import ShopListView, ShopDetailView

app_name = 'shop'

urlpatterns = [
    path('', ShopListView.as_view(), name='shop-list'),
    path('<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
]
