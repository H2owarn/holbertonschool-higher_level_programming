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
    if username not in users:
        return jsonify({"error": "User not found"}), 400

    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify(user_data)

@app.route("/status")
def status():
    return "OK"

@app.route("/add_user", methods=["POST"])
def add_user():

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400


    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username:
        return jsonify({"error": "Username is required"}), 400

  # for duplicate usernames — overwrite

    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }

    response_data = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({"message": "User added", "user": response_data}), 201


if __name__ == "__main__":
    app.run(port=5000)