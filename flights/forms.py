from django import forms
from flights.models import Passenger

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()

class ManageBookingForm(forms.Form):
    booking_code = forms.UUIDField()