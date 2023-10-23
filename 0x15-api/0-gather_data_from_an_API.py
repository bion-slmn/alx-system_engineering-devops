#!/usr/bin/python3
'''THis script uses a RESTAPI to collect information
of an employee'''
import requests
import sys


if __name__ == '__main__':
    employee_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    payload = {"userId": employee_ID}
    user_response = requests.get(f'{url}/users/{employee_ID}').json()
    todo_response = requests.get(f'{url}/todos/', params=payload).json()

    employee_name = user_response.get('name')
    total_task = len(todo_response)

    task_completd = filter(lambda x: x.get("completed") is True,
                           todo_response)
    task_completd_list = list(task_completd)

    print(f'Employee {employee_name} is done with tasks\
          ({len(task_completd_list)}/{total_task}):')

    for task in task_completd_list:
        print(f'\t {task.get("title")}')
