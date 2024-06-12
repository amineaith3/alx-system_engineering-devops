#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]

    user = requests.get(f"{url}/users/{id}").json()
    todos = requests.get(f"{url}/todos/?userId={id}").json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({len(completed)}/{len(todos)}):")

    [print(f"\t {c}") for c in completed]
