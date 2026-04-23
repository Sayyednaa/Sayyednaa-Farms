from django.contrib import admin
from .models import Supplier, InventoryItem, StockTransaction

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'is_low_stock')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('item', 'transaction_type', 'quantity', 'date')
    list_filter = ('transaction_type', 'date')
