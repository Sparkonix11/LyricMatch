from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .song import Song

def init_db(app):
    with app.app_context():
        db.create_all()