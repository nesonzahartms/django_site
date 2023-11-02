from django.urls import path
from . import views
from django.urls import path
from .views import hotel_search, create_review, hotel_gallery
from .views import agency_login, agency_registration

urlpatterns = [
    path('hotels/', views.HotelListView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('hotels/search/', hotel_search, name='hotel_search'),
    path('hotels/<int:hotel_id>/gallery/', hotel_gallery, name='hotel_gallery'),
    path('agencies/<int:agency_id>/reviews/create/', create_review, name='create_review'),
    path('login/', agency_login, name='agency_login'),
    path('register/', agency_registration, name='agency_registration'),

]
