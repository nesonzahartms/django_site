from django.urls import path
from . import views

urlpatterns = [
    path('hotels/<int:hotel_id>/book/', views.make_reservation, name='make_reservation'),
    path('reservations/<int:reservation_id>/', views.view_reservation, name='view_reservation'),
]
