#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)

#  When someone visits the / endpoint

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def username():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/status")
def status():
    return "OK"

@app.route("/add_user", methods=["POST"])
def add_user():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    print(f"User name: {username}")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(port=5000)