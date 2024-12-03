from flask import Flask
from backend.models import db, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
db.init_app(app)

with app.app_context():
    db.create_all() # Создает все таблицы на основе моделей

# Импортируем маршруты после создания экземпляра db
from routes.routes import *

if __name__ == '__main__':
    app.run(debug=True)

