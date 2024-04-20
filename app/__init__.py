from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('local_settings')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views import cliente_view
from .models import cliente_models
