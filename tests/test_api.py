import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import os
from datetime import datetime, timedelta
from app import create_app, db
from app.models import Flight, Booking

@pytest.fixture
def app():
    os.environ['DATABASE_URL'] = 'postgresql://airline_user:airline_password@localhost:5432/airline_db_test'
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_flight(app):
    flight = Flight(
        flight_number='FL123',
        origin='New York',
        destination='London',
        departure_time=datetime.utcnow(),
        arrival_time=datetime.utcnow() + timedelta(hours=8),
        available_seats=100
    )
    db.session.add(flight)
    db.session.commit()
    return flight

def test_get_flights(client, sample_flight):
    response = client.get('/api/flights')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['flight_number'] == 'FL123'

def test_get_flight(client, sample_flight):
    response = client.get(f'/api/flights/{sample_flight.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['flight_number'] == 'FL123'

def test_create_booking(client, sample_flight):
    booking_data = {
        'flight_id': sample_flight.id,
        'passenger_name': 'John Doe',
        'passenger_email': 'john@example.com'
    }
    response = client.post('/api/bookings', json=booking_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['passenger_name'] == 'John Doe'
    assert data['flight_id'] == sample_flight.id 