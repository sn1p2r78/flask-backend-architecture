from flask import Flask
from flask.sqlalchemy import SQLAlchemy
from flask.bcrypt import Bcrypt
from flask.login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask.socketio import SocketIO
import requests
import random
import string

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
socketio = SocketIO()

# Define app
def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URII] = 'sqlite:///database.db'
    app.config['SQLALSDEV_TRANCK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.service import service_bp
    from app.routes.microsoft_graph import microsoft_graph_bp

