# Airline System

A modern airline booking system built with Flask, PostgreSQL, and Docker, featuring monitoring with Prometheus and Grafana.

## Features

- Flight management
- Booking system
- RESTful API
- PostgreSQL database
- Docker containerization
- Monitoring with Prometheus and Grafana
- CI/CD pipeline with GitHub Actions

## Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Git

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd airline-system
```

2. Start the application using Docker Compose:
```bash
docker-compose up --build
```
The project structure is:
airline_system/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── templates/
│   └── static/
├── tests/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
└── README.md

The application will be available at:
- Web API: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)

## API Endpoints

- GET /api/flights - List all flights
- GET /api/flights/<id> - Get flight details
- POST /api/bookings - Create a new booking

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest
```

## Monitoring

The application includes monitoring with Prometheus and Grafana:

- Prometheus collects metrics from the Flask application
- Grafana provides visualization of the metrics
- Default Grafana credentials: admin/admin

## CI/CD

The project uses GitHub Actions for continuous integration and deployment:

- Automated testing
- Code linting
- Docker image building and pushing
- Deployment to production (when configured)

## Security

- Non-root user in Docker container
- Secure database credentials
- Environment variables for sensitive data

## License

MIT 