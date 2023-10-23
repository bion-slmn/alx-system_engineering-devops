#!/usr/bin/python3
'''THis script uses a RESTAPI to collect information
of an employee and writes it to a .csv file'''
import json
import requests
import sys


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(url + '/users').json()
    all_todos = {}

    for user in user_response:
        employee_name = user.get("username")
        employee_ID = user.get('id')

        payload = {"userId": employee_ID}

        todos = requests.get(url + '/todos', params=payload).json()

        todo_dict = {employee_ID: [{
                                    "task": task.get("title"),
                                    "completed": task.get("completed"),
                                    "username": employee_name
                        }for task in todos]}

        all_todos.update(todo_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_todos, json_file)
