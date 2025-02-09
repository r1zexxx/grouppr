from django.shortcuts import render
from .models import Booking


# Create your views here.
def main(request):
    book = Booking.objects.all()
    return render(request, "main.html", {"bookings": book})

def book_detail_view(reguest, book_id):
    book = Booking.objects.get(id=book_id)
    return render(reguest, "booking.html", {"booking": [book]})