from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import ParkingSlot, generate_code
import json

def welcome(request):
    stats = {}
    for entrance in ['South', 'East', 'North']:
        stats[entrance] = ParkingSlot.objects.filter(entrance=entrance, status='available').count()
    total_available = ParkingSlot.objects.filter(status='available').count()
    total_slots = ParkingSlot.objects.count()
    return render(request, 'parking/welcome.html', {
        'stats': stats,
        'total_available': total_available,
        'total_slots': total_slots,
    })

def choose_entrance(request):
    stats = {}
    for entrance in ['South', 'East', 'North']:
        stats[entrance] = ParkingSlot.objects.filter(entrance=entrance, status='available').count()
    return render(request, 'parking/entrance.html', {'stats': stats})

def choose_level(request, entrance):
    level_stats = {}
    for level in [1, 2, 3]:
        level_stats[level] = ParkingSlot.objects.filter(entrance=entrance, level=level, status='available').count()
    return render(request, 'parking/level.html', {
        'entrance': entrance,
        'level_stats': level_stats,
    })

def slots(request, entrance, level):
    all_slots = ParkingSlot.objects.filter(entrance=entrance, level=int(level))
    available_count = all_slots.filter(status='available').count()
    return render(request, 'parking/slots.html', {
        'slots': all_slots,
        'entrance': entrance,
        'level': level,
        'available_count': available_count,
    })

@require_POST
def confirm_slot(request):
    data = json.loads(request.body)
    slot_id = data.get('slot_id')
    try:
        slot = ParkingSlot.objects.get(slot_id=slot_id, status='available')
        code = generate_code()
        slot.status = 'occupied'
        slot.verification_code = code
        slot.occupied_at = timezone.now()
        slot.save()
        request.session['last_slot'] = slot_id
        request.session['last_code'] = code
        return JsonResponse({
            'success': True,
            'slot_id': slot_id,
            'code': code,
            'entrance': slot.entrance,
            'level': slot.level,
            'time': slot.occupied_at.strftime('%d %b %Y, %H:%M'),
        })
    except ParkingSlot.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Slot not available.'})

def receipt(request):
    slot_id = request.session.get('last_slot')
    code = request.session.get('last_code')
    if not slot_id:
        return redirect('welcome')
    try:
        slot = ParkingSlot.objects.get(slot_id=slot_id)
        return render(request, 'parking/receipt.html', {
            'slot': slot,
            'code': code,
        })
    except ParkingSlot.DoesNotExist:
        return redirect('welcome')

def exit_form(request):
    return render(request, 'parking/exit.html')

@require_POST
def verify_exit(request):
    slot_id = request.POST.get('slot_id', '').strip().upper()
    code = request.POST.get('code', '').strip().upper()
    try:
        slot = ParkingSlot.objects.get(slot_id=slot_id)
        if slot.status != 'occupied':
            return render(request, 'parking/exit.html', {
                'error': 'This slot is not currently occupied.',
                'slot_id': slot_id,
            })
        if slot.verification_code != code:
            return render(request, 'parking/exit.html', {
                'error': 'Incorrect verification code. Access denied. Please try again.',
                'slot_id': slot_id,
            })
        slot.status = 'available'
        slot.verification_code = None
        slot.occupied_at = None
        slot.save()
        return redirect('thankyou')
    except ParkingSlot.DoesNotExist:
        return render(request, 'parking/exit.html', {
            'error': 'Slot number not found. Please check and try again.',
            'slot_id': slot_id,
        })

def thankyou(request):
    return render(request, 'parking/thankyou.html')

def parked(request):
    slot_id = request.session.get('last_slot')
    code = request.session.get('last_code')
    return render(request, 'parking/parked.html', {'slot_id': slot_id, 'code': code})
