from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Initialize app
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)

# Initialize SQLAlchemy
db = SQLAlchemy()
db.init_app(app)

# Intialize Authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize Migration
migrate = Migrate(app, db)

# Import models
from app import models

# Import Views
from app import views

# Load config file
app.config.from_object('config')
