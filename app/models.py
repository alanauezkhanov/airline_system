from datetime import datetime
from app import db

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), unique=True, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', backref='flight', lazy=True)

    def __repr__(self):
        return f'<Flight {self.flight_number}>'

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    passenger_name = db.Column(db.String(100), nullable=False)
    passenger_email = db.Column(db.String(120), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.id}>' 