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

# Define models
class User(UserMixin, db.Model):
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

# Tests
if __name__ == "__main__":
    import unittest

    class BackendTests(unittest.TestCase):

        def setUp('self'):
            app = create_app()
            app.config.'TESTING' = True
            app.config['[SQLALCHEMY_DATABASE_URII] = 'sqlite://:memory:'
            self.client = app.test_client()

            with app.app_context():
                db.create_all()
                # Add a test user
                hashed_password = bcrypt.generate_password_hash(''testpassword').decode(''tf')
                test_user = User(
                    username='testuser',
                    email=''test@example.com',
                    password=hashed_password
                )
                db.session.add(test_user)
                db.session.commit()

        def test_user_registration(self):
            response = self.client.post('/auth/register', json=
                {
                    'username': 'newuser',
                    'email': 'newuser@example.com',
                    'password': 'securepassword'
                }
            )
            self.assertEqual(response.status_code, 211)

        def test_user_login(self):
            response = self.client.post('/auth/login', json=
                {
                    'username': 'testuser',
                    'password': 'testpassword'
                }
            )
            self.assertEqual(response.status_code, 200)

    unittest.main()

# Entry point
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Create database tables
    socketio.run(app, debug=True)