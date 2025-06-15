#!/usr/bin/python3

"""
Flask authentication demo with:
• Basic Auth
• JWT Authentication
• Role-based Access Control
"""



from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity



app = Flask(__name__)


# ─────────── Config ────────────

app.config['SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)


# ─────────── User store ────────
users = {

    "user1": {"username": "user1", "password": generate_password_hash("password"),
                "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"),
                "role": "admin"}
    }

# ─────────── User store ────────
auth = HTTPBasicAuth()

@auth.verify_password
def verify_pass(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username   # ← tells HTTPAuth “login succeeded”

    return None   # ← fail

# ─────────── Routes ────────────

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

@app.route('/login', methods=['POST'])
def login():

    """
    curl -X POST -H "Content-Type: application/json" \
         -d '{"username":"user1","password":"password"}' \
         http://127.0.0.1:5000/login
    """


    auth = request.get_json(force=True)
    username = auth.get("username", "")
    password = auth.get("password", "")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_access_token(identity={
        "username" : username,
        "role" : user["role"]
    })

    return jsonify(access_token=token), 200



@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route("/admin_only", methods=["GET"])
@jwt_required()
def admin_only():
    who = get_jwt_identity()

    if who["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


def role_required(role_name):
    """Decorator to enforce role-based access."""

    def decorator(fn):
        @jwt_required()
        def wrapper(*args, **kwargs):
            ident = get_jwt_identity()         # {'username': 'user1', 'role': 'user'}

            if ident["role"] != role_name:
                return jsonify({"error": "Forbidden – Requires role: " + role_name}), 403

            return fn(*args, **kwargs)
        wrapper.__name__ = fn.__name__

        return wrapper
    return decorator

# ─────────── Run ───────────────

if __name__ == "__main__":
    app.run(debug=True)
