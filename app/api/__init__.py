import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',  # <-- сначала ищет переменную окружения
        'postgresql://airline_user:airline_password@db:5432/airline_db'  # <-- если переменной нет, только тогда db
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # ... остальной код ...