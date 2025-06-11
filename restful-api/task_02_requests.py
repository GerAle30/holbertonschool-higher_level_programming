import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if rerponse.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

            def fetch_and_save_posts():
                """Fetches posts and saves them into a csv file"""
                url = "https://jsonplaceholder.typicode.com/posts"
                response = requests.get(url)

                if response.status_code == 200:
                    posts = response.json()
                    data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

                    with open("posts.csv, mode="w", newline="", endcoding="utf-8") as csvfile:
                        fieldnames = ["id", "tutle", "body"]
                         write = csv.DictWrite(csvfile, fieldnames=fieldnames)

                         write.writeheade()
                         for post in data:
                             writer.writerow(post)
