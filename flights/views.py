from django.shortcuts import render, redirect, get_object_or_404
from flights.models import Flight, Airport, Passenger, Booking
from django.http import HttpResponse
from flights.forms import BookingForm, ManageBookingForm

def index(request):
    flights = Flight.objects.all()
    airports = Airport.objects.all()
    return render(request, 'flights/index.html', {'flights': flights, 'airports': airports})

def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    bookings = flight.booking_set.all()
    return render(request, 'flights/flight.html', {'flight': flight, 'bookings': bookings})

def book(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            passenger, created = Passenger.objects.get_or_create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            booking = Booking.objects.create(passenger=passenger, flight=flight)
            return redirect('booking_confirmation', booking_code=booking.booking_code)
    else:
        form = BookingForm()
    return render(request, 'flights/book.html', {'flight': flight, 'form': form})

def booking_confirmation(request, booking_code):
    booking = get_object_or_404(Booking, booking_code=booking_code)
    return render(request, 'flights/booking_confirmation.html', {'booking': booking})

def manage_booking(request):
    if request.method == 'POST':
        form = ManageBookingForm(request.POST)
        if form.is_valid():
            booking_code = form.cleaned_data['booking_code']
            try:
                booking = Booking.objects.get(booking_code=booking_code)
                return render(request, 'flights/booking_details.html', {'booking': booking})
            except Booking.DoesNotExist:
                return render(request, 'flights/error.html', {'error_message': "Invalid booking code."})
    else:
        form = ManageBookingForm()
    return render(request, 'flights/manage_booking.html', {'form': form})

def airport(request, airport_code):
    airport = get_object_or_404(Airport, code=airport_code)
    departures = airport.departures.all()
    arrivals = airport.arrivals.all()
    return render(request, 'flights/airport.html', {'airport': airport, 'departures': departures, 'arrivals': arrivals})
