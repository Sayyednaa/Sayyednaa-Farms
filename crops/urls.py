from django.urls import path
from .views import (
    CropsIndexView, CropCreateView, 
    CropUpdateView, CropDeleteView
)

app_name = 'crops'

urlpatterns = [
    path('', CropsIndexView.as_view(), name='index'),
    path('add/', CropCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', CropUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CropDeleteView.as_view(), name='delete'),
]
