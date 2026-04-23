from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Feed', 'Feed'),
        ('Medicine', 'Medicine'),
        ('Tools', 'Tools'),
        ('Fertilizer', 'Fertilizer'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    unit = models.CharField(max_length=20, help_text="e.g. kg, liters, units")
    quantity = models.FloatField(default=0)
    min_stock_level = models.FloatField(default=10, help_text="Alert level")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_stock_level

class StockTransaction(models.Model):
    TRANS_TYPE_CHOICES = [
        ('In', 'Stock In (Purchase/Addition)'),
        ('Out', 'Stock Out (Usage/Sale)'),
    ]

    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANS_TYPE_CHOICES)
    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'In':
            self.item.quantity += self.quantity
        else:
            self.item.quantity -= self.quantity
        self.item.save()
        super().save(*args, **kwargs)
