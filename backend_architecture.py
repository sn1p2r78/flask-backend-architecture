from flask import Flask
from flask.sqlalchemy import SQLAlchemy
from flask.bcrypt import Bcrypt
from flask.login import LoginManager
from flask.socketio import SocketIO

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLPALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(service_bp, url_prefix='/service')
    app.register_blueprint(microsoft_graph_bp, url_prefix='/microsoft-graph')

    return app

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150, nullable=False, unique=True)
    email = db.Column(db.String(150, nullable=False, unique=True)
    password = db.Column(db.String(200, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.Foreign(\'user.id\'))


class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreign(\"user.id\"))
    service_id = db.Column(db.Integer, db.Foreign(\"service.id\"))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    details = db.Column(db.Text, nullable=True)

# Directory structure
# app/
#   __init__.py
#   routes/
#     __init__.py
#   �� � auth.py
#   ₂ admin.py
#     service.py
#   ₂ microsoft_graph.py
#   templates/
#     index.html
# tests/
# requirements.txt

# Entry point
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Create database tables
    socketio.run(app, debug=True)