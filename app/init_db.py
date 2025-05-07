from app import create_app, db
from app.models import Flight
from datetime import datetime, timedelta

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Add sample flights if none exist
        if Flight.query.count() == 0:
            flights = [
                Flight(
                    flight_number='FL101',
                    origin='New York',
                    destination='London',
                    departure_time=datetime.utcnow() + timedelta(days=1),
                    arrival_time=datetime.utcnow() + timedelta(days=1, hours=8),
                    available_seats=100
                ),
                Flight(
                    flight_number='FL102',
                    origin='London',
                    destination='Paris',
                    departure_time=datetime.utcnow() + timedelta(days=2),
                    arrival_time=datetime.utcnow() + timedelta(days=2, hours=2),
                    available_seats=150
                ),
                Flight(
                    flight_number='FL103',
                    origin='Paris',
                    destination='Berlin',
                    departure_time=datetime.utcnow() + timedelta(days=3),
                    arrival_time=datetime.utcnow() + timedelta(days=3, hours=3),
                    available_seats=120
                )
            ]
            db.session.add_all(flights)
            db.session.commit()
            print("Sample flights added to database")

if __name__ == '__main__':
    init_db() 