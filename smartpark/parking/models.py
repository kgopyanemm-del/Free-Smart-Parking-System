from django.db import models
import random
import string

def generate_code():
    chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    return ''.join(random.choices(chars, k=6))

class ParkingSlot(models.Model):
    ENTRANCE_CHOICES = [('South', 'South'), ('East', 'East'), ('North', 'North')]
    LEVEL_CHOICES = [(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')]
    STATUS_CHOICES = [('available', 'Available'), ('occupied', 'Occupied')]

    slot_id = models.CharField(max_length=20, unique=True)
    entrance = models.CharField(max_length=10, choices=ENTRANCE_CHOICES)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    slot_number = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    verification_code = models.CharField(max_length=10, blank=True, null=True)
    occupied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.slot_id} - {self.status}"

    class Meta:
        ordering = ['entrance', 'level', 'slot_number']
