from django.urls import path
from .views import DeliveryListCreateAPIView, DeliveryDetailAPIView

urlpatterns = [
    path('', DeliveryListCreateAPIView.as_view(), name='delivery-list-create'),
    path('<int:pk>/', DeliveryDetailAPIView.as_view(), name='delivery-detail'),
]
