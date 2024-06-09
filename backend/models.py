from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    rides = db.relationship('Ride', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        # Flask-Login requires this property
        return True

    def get_id(self):
        # Flask-Login requires this method
        return self.id

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String(120), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(9), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'departure': self.departure,
            'destination': self.destination,
            'date': self.date,
            'time': self.time,
            'passengers': self.passengers,
            'phone_number': self.phone_number,
            'user_id': self.user_id,
            'user': self.user.to_dict()
        }
