from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, init_db
from apis import init_apis


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    init_db(app)
    migrate = Migrate(app, db)

    init_apis(app)
    return app