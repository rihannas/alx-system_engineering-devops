#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    API = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) > 1:
        userId = sys.argv[1]
        user = requests.get('{}/users/{}'.format(API, userId)).json()
        userTodo = requests.get('{}/todos'.format(API)).json()
        todoUser = {}
        taskList = []

        for task in userTodo:
            if task.get('userId') == int(userId):
                taskDict = {"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": user.get('username')}
                taskList.append(taskDict)
        todoUser[userId] = taskList

        filename = userId + '.json'
        with open(filename, mode='w') as f:
            json.dump(todoUser, f)
