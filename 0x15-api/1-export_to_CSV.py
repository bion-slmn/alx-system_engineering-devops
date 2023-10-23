#!/usr/bin/python3
'''THis script uses a RESTAPI to collect information
of an employee and writes it to a .csv file'''
import csv
import requests
import sys


if __name__ == '__main__':
    employee_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    payload = {"userId": employee_ID}
    user_response = requests.get(f'{url}/users/{employee_ID}').json()
    todo_response = requests.get(f'{url}/todos/', params=payload).json()

    employee_name = user_response.get('name')
    file_name = f'{employee_ID}.csv'

    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in todo_response:
            writer.writerow([employee_ID, employee_name,
                            x.get("completed"), x.get("title")])
