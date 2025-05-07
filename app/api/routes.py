from flask import jsonify, request
from app.api import bp
from app.models import Flight, Booking
from app import db

@bp.route('/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([{
        'id': flight.id,
        'flight_number': flight.flight_number,
        'origin': flight.origin,
        'destination': flight.destination,
        'departure_time': flight.departure_time.isoformat(),
        'arrival_time': flight.arrival_time.isoformat(),
        'available_seats': flight.available_seats
    } for flight in flights])

@bp.route('/flights/<int:id>', methods=['GET'])
def get_flight(id):
    flight = Flight.query.get_or_404(id)
    return jsonify({
        'id': flight.id,
        'flight_number': flight.flight_number,
        'origin': flight.origin,
        'destination': flight.destination,
        'departure_time': flight.departure_time.isoformat(),
        'arrival_time': flight.arrival_time.isoformat(),
        'available_seats': flight.available_seats
    })

@bp.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    flight = Flight.query.get_or_404(data['flight_id'])
    
    if flight.available_seats < 1:
        return jsonify({'error': 'No available seats'}), 400
    
    booking = Booking(
        flight_id=data['flight_id'],
        passenger_name=data['passenger_name'],
        passenger_email=data['passenger_email']
    )
    
    flight.available_seats -= 1
    db.session.add(booking)
    db.session.commit()
    
    return jsonify({
        'id': booking.id,
        'flight_id': booking.flight_id,
        'passenger_name': booking.passenger_name,
        'passenger_email': booking.passenger_email,
        'booking_date': booking.booking_date.isoformat()
    }), 201 