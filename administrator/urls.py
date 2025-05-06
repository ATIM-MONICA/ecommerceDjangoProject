from django.urls import path
from .views import AdministratorListCreateAPIView, AdministratorDetailAPIView

urlpatterns = [
    path('', AdministratorListCreateAPIView.as_view(), name='administrator-list-create'),
    path('<int:pk>/', AdministratorDetailAPIView.as_view(), name='administrator-detail'),
]
