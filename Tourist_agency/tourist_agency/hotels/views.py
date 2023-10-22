from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hotel


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/reservation.html'
# Create your views here.
