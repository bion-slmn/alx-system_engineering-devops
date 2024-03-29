#!/usr/bin/python3
'''THis script uses a RESTAPI to collect information
of an employee and writes it to a .csv file'''
import json
import requests
import sys


if __name__ == '__main__':
    employee_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    payload = {"id": employee_ID}
    pay = {"userId": employee_ID}

    user_response = requests.get(url + '/users', params=payload).json()
    todos = requests.get(url + '/todos', params=pay).json()

    employee_name = user_response[0].get("username")
    file_name = '{}.json'.format(employee_ID)

    todo_dict = {employee_ID: [{
                                "task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": employee_name
                    }for task in todos]}

    with open(file_name, 'w') as json_file:
        json.dump(todo_dict, json_file)
