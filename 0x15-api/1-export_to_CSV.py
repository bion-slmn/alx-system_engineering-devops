#!/usr/bin/python3
'''THis script uses a RESTAPI to collect information
of an employee and writes it to a .csv file'''
import csv
import requests
import sys


if __name__ == '__main__':
    employee_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    payload = {"id": employee_ID}
    pay = {"userId": employee_ID}
    user_response = requests.get(f'{url}/users/', params=payload).json()

    todo_response = requests.get(f'{url}/todos/', params=pay).json()

    employee_name = user_response[0].get("username")
    file_name = f'{employee_ID}.csv'

    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in todo_response:
            writer.writerow([employee_ID, employee_name,
                            x.get("completed"), x.get("title")])
