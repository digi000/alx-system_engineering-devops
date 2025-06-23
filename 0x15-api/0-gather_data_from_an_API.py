#!/usr/bin/python3

"""0. Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    urId = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{urId}')
    userDt = user.json()
    userName = userDt['name']
    tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={urId}')
    tasksDt = tasks.json()
    tasksTotal = len(tasksDt)
    tasksCp = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={urId}&&completed=true')
    tasksCd = tasksCp.json()
    tasksCc = len(tasksCd)
    print(f"Employee {userName} is done with tasks({tasksCc}/{tasksTotal})")
    for task in tasksCd:
        print(f"\t {task['title']}")
