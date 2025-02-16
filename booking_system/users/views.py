from django.shortcuts import render
from .models import Booking, Rooms


# Create your views here.
def main(request):
    bookin = Booking.objects.all()
    return render(request, "main.html", {"bookings": bookin})

def bookin(reguest, bookin_id):
    bookin = Booking.objects.get(id=bookin_id)
    return render(reguest, "booking.html", {"booking": [bookin]})

def rooms(reguest, rooms_id):
    rooms = Rooms.objects.get(id=rooms_id)
    return render(reguest, "rooms.html", {"rooms": [rooms]})
