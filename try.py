import os
import sys

import requests

print(sys.version)
print (sys.executable)

name = input("Your name:")


def greeting(person):
    greeting = "Hello, {}!".format(person)
    return greeting


print(greeting(name))
