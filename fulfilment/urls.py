from django.urls import path
from .views import FulfilmentListCreateAPIView, FulfilmentDetailAPIView

urlpatterns = [
    path('', FulfilmentListCreateAPIView.as_view(), name='fulfilment-list-create'),
    path('<int:pk>/', FulfilmentDetailAPIView.as_view(), name='fulfilment-detail'),
]
