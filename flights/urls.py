from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("airport/<str:airport_code>", views.airport, name="airport"),
]