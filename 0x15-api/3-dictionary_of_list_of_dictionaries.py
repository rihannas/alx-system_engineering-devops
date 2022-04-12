#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    API = "https://jsonplaceholder.typicode.com"

    users = requests.get('{}/users'.format(API)).json()
    userTodo = requests.get('{}/todos'.format(API)).json()
    userTodoData = {}

    for user in users:
        taskList = []
        for task in userTodo:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        userTodoData[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(userTodoData, f)
