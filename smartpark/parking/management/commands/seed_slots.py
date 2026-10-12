from django.core.management.base import BaseCommand
from parking.models import ParkingSlot

class Command(BaseCommand):
    help = 'Seed parking slots into the database'

    def handle(self, *args, **kwargs):
        ParkingSlot.objects.all().delete()
        entrances = ['South', 'East', 'North']
        levels = [1, 2, 3]
        count = 0
        for entrance in entrances:
            for level in levels:
                for num in range(1, 51):
                    slot_id = f"{entrance[0]}-L{level}-{str(num).zfill(3)}"
                    ParkingSlot.objects.create(
                        slot_id=slot_id,
                        entrance=entrance,
                        level=level,
                        slot_number=num,
                        status='available',
                    )
                    count += 1
        self.stdout.write(self.style.SUCCESS(f'Created {count} parking slots.'))
