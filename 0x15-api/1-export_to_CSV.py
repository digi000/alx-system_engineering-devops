#!/usr/bin/python3

"""1. Export to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    urId = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{urId}')
    userDt = user.json()
    userName = userDt['username']
    todo = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={urId}')
    todoDt = todo.json()
    with open(f"{urId}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        for task in todoDt:
            writer.writerow(["{}".format(urId), f"{userName}", f"{task['completed']}", f'{task["title"]}'])
