from django.contrib import admin
from .models import Category, Breed, Livestock, HealthRecord

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'breed', 'status', 'date_of_birth')
    list_filter = ('status', 'breed__category')
    search_fields = ('identifier',)

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('livestock', 'date', 'diagnosis')
    list_filter = ('date',)
