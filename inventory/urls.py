from django.urls import path
from .views import (
    InventoryListView, InventoryCreateView, InventoryUpdateView, 
    InventoryDeleteView, StockTransactionCreateView
)

app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='list'),
    path('add/', InventoryCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', InventoryUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', InventoryDeleteView.as_view(), name='delete'),
    path('transaction/add/', StockTransactionCreateView.as_view(), name='transaction_add'),
]
