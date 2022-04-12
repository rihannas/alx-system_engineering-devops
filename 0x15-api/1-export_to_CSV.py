#!/usr/bin/python3
""" a Python script that, uses an API,
for a given employee ID,
to export dara in CSV format.
"""
if __name__ == "__main__":

    import requests
    import sys
    import csv

    API = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) > 1:
        userId = sys.argv[1]
        user = requests.get('{}/users/{}'.format(API, userId)).json()
        userName = user.get('username')
        userTodo = requests.get('{}/todos'.format(API)).json()

        filename = userId + '.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')
            for task in userTodo:
                if task.get('userId') == int(userId):
                    writer.writerow([userId, userName,
                                     str(task.get('completed')),
                                     task.get('title')])
