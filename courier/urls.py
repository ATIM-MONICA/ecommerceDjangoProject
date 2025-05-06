from django.urls import path
from .views import CourierListCreateAPIView, CourierDetailAPIView

urlpatterns = [
    path('', CourierListCreateAPIView.as_view(), name='courier-list-create'),
    path('<int:pk>/', CourierDetailAPIView.as_view(), name='courier-detail'),

]

