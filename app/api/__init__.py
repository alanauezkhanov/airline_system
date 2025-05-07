from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import routes
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql://airline_user:airline_password@db:5432/airline_db'
    )
    # ...