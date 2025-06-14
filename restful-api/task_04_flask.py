#!/usr/bin/python3
"""
A simple Flask API to handle basic user data with GET and POST endpoints.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Root endpoint returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Status endpoint returns OK."""
    return "OK"


@app.route('/data')
def get_usernames():
    """Return a list of all usernames stored in the users dictionary."""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """
    Return the full object for a given username.
    If not found, return an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handle POST requests to add a new user to the users dictionary.
    Return a 201 on success or 400 if username is missing.
    """
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == '__main__':
    app.run()
