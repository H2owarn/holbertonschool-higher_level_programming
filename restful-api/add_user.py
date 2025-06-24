#!/usr/bin/python3

import requests

# Your robot’s URL
url = "http://localhost:5000/add_user"

# The note you want to send
data = {
    "username": "john",
    "name": "Emma",
    "age": 30,
    "city": "New York"
}

# Send the note!
response = requests.post(url, json=data)

# Show what your robot says back
print(response.json())