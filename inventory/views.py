from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import InventoryItem, StockTransaction, Supplier

class InventoryListView(LoginRequiredMixin, ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'items'
    login_url = 'core:login'

class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = InventoryItem
    fields = ['name', 'category', 'unit', 'quantity', 'min_stock_level', 'supplier']
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')
    login_url = 'core:login'

class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    fields = ['name', 'category', 'unit', 'quantity', 'min_stock_level', 'supplier']
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')
    login_url = 'core:login'

class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:list')
    login_url = 'core:login'

class StockTransactionCreateView(LoginRequiredMixin, CreateView):
    model = StockTransaction
    fields = ['item', 'transaction_type', 'quantity', 'notes']
    template_name = 'inventory/transaction_form.html'
    success_url = reverse_lazy('inventory:list')
    login_url = 'core:login'
