#!/usr/bin/python3
'''Script'''

import requests
import sys

def get_employee_todo_progress(employee_id):
    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    employee = user_response.json()
    employee_name = employee.get('name')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Calculate TODO progress
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Print the TODO progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
