from flask import current_app as app, jsonify
from flask_security import auth_required, roles_required
from .models import User, db

@app.get('/')
def home():
    return "Hello World"

@app.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return "Hello Admin"

@app.get('/activate/user/<int:user_id>')
@auth_required("token")
@roles_required("admin")
def activate_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.active = True
    db.session.commit()
    return jsonify({"message": "User Activated"})