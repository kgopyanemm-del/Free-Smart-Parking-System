from django.contrib import admin
from .models import ParkingSlot

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ['slot_id', 'entrance', 'level', 'slot_number', 'status', 'verification_code', 'occupied_at']
    list_filter = ['entrance', 'level', 'status']
    search_fields = ['slot_id', 'verification_code']
