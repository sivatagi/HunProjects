import os
import sys

import requests


name = input("Your name:")


def greeting(person):
    greeting = "Hello, {}!".format(person)
    return greeting


print(greeting(name))
