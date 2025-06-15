#!/usr/bin/python3

from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_secret_key"  # keep this secure
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Simulated user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ─────────── BASIC AUTH ───────────
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user  # must return user object, not just username

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/debug-auth")
def debug_auth():
    auth_header = request.headers.get("Authorization")
    return jsonify({"Authorization": auth_header})


# ─────────── JWT AUTH ───────────
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON file")

    for key in ["username", "password"]:
        if key not in data:
            abort(400, f"Missing attribute {key}.")

    user = users.get(data["username"])
    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"msg": "Wrong username or password"}), 401

    token = create_access_token(identity=data["username"])
    return jsonify(access_token=token)

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    curr_user = get_jwt_identity()
    user = users.get(curr_user)
    if not user or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# ─────────── JWT ERROR HANDLERS ───────────
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# ─────────── RUN ───────────
if __name__ == "__main__":
    app.run()
