import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in data:
                writer.writerow(post)

