from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

from booking.models import Reservation


@login_required
def make_reservation(request, hotel_id):
    # Обработка формы бронирования
    return render(request, 'booking/reservation.html')


@login_required
def view_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    return render(request, 'booking/reservation_detail.html', {'reservation': reservation})

# Create your views here.
