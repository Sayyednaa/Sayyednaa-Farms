from django.urls import path
from .views import (
    LivestockIndexView, LivestockCreateView, 
    LivestockUpdateView, LivestockDeleteView
)

app_name = 'livestock'

urlpatterns = [
    path('', LivestockIndexView.as_view(), name='index'),
    path('add/', LivestockCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', LivestockUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', LivestockDeleteView.as_view(), name='delete'),
]
