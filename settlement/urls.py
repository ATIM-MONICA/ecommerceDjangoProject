from django.urls import path
from .views import SettlementListCreateAPIView, SettlementDetailAPIView

urlpatterns = [
    path('', SettlementListCreateAPIView.as_view(), name='settlement-list-create'),
    path('<int:pk>/', SettlementDetailAPIView.as_view(), name='settlement-detail'),
]
