#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSON"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        posts_data = [{'id': p['id'], 'title': p['title'], 'body': p['body']} for p in posts]

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
