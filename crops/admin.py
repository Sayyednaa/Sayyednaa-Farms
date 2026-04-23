from django.contrib import admin
from .models import CropType, Variety, Plantation, Harvest

@admin.register(CropType)
class CropTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'crop_type')
    list_filter = ('crop_type',)

@admin.register(Plantation)
class PlantationAdmin(admin.ModelAdmin):
    list_display = ('variety', 'location', 'planting_date', 'status')
    list_filter = ('status', 'variety__crop_type')

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ('plantation', 'date', 'quantity')
    list_filter = ('date',)
