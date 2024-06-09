from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
CORS(app, supports_credentials=True)

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    login_user(user)
    session['username'] = user.username  # Zapisz nazwę użytkownika w sesji
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    session.pop('username', None)  # Usuń nazwę użytkownika z sesji
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/current_user', methods=['GET'])
@login_required
def get_current_user():
    username = session.get('username')
    return jsonify({"username": username, "email": current_user.email}), 200

if __name__ == '__main__':
    app.run()
