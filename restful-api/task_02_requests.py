#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        simplified_data = []
        for post in posts:
            simplified_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        #  Write the data to a CSV file
        with open("posts.csv", mode='w', newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(simplified_data)

        print("Posts saved to posts.csv")

    else:
        print("Failed to fetch posts")
