#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)

#  When someone visits the / endpoint

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}

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

    username = data.get("username")

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(port=5000)