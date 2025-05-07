import os
import time
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prometheus_client import Counter, Histogram, REGISTRY

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Используем DATABASE_URL из окружения, если она есть
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql://airline_user:airline_password@db:5432/airline_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Prometheus metrics (регистрируем только если ещё не зарегистрированы)
    if not any(m.name == 'http_requests_total' for m in REGISTRY.collect()):
        global REQUEST_COUNT, REQUEST_LATENCY
        REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
        REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

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