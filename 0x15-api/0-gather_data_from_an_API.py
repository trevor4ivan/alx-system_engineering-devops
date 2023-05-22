#!/usr/bin/python3
"""A script that uses a REST API to print todo list."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    items = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [i.get("title") for i in items if i.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(items)))
    [print("\t {}".format(item)) for item in completed]
