from django.urls import path
from .views import PredictionList, PredictionDetail

urlpatterns = [
    # Nama 'prediction-list' dan 'prediction-detail' dipakai oleh fungsi reverse() di serializers.py
    path('predictions/', PredictionList.as_view(), name='prediction-list'),
    path('predictions/<uuid:pk>/', PredictionDetail.as_view(), name='prediction-detail'),
]