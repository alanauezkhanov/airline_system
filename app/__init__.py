from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prometheus_client import Counter, Histogram
import time

db = SQLAlchemy()
migrate = Migrate()

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://airline_user:airline_password@db:5432/airline_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/api/flights', methods=['GET'])
    def get_flights():
    
    # Register blueprints
    # from app.api import bp as api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')
    
    # Add middleware for Prometheus metrics
    @app.before_request
    def before_request():
        request.start_time = time.time()
    
    @app.after_request
    def after_request(response):
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.endpoint,
            status=response.status_code
        ).inc()
        
        REQUEST_LATENCY.observe(time.time() - request.start_time)
        return response
    
    return app 