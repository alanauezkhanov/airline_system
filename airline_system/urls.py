from django.urls import path
from flights import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights/<int:flight_id>/', views.flight, name='flight'),
    path('flights/<int:flight_id>/book/', views.book, name='book'),
    path('booking/<uuid:booking_code>/', views.booking_confirmation, name='booking_confirmation'),
    path('manage-booking/', views.manage_booking, name='manage_booking'),
    path('airports/<str:airport_code>/', views.airport, name='airport'),
]