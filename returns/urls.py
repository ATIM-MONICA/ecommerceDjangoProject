from django.urls import path
from .views import ReturnRequestListCreateAPIView, ReturnRequestDetailAPIView

urlpatterns = [
    path('', ReturnRequestListCreateAPIView.as_view(), name='return-list-create'),
    path('<int:pk>/', ReturnRequestDetailAPIView.as_view(), name='return-detail'),
]
