# Scripting
import datetime
import os
# Shorter pieces of code that allow us to do things via code that otherwise we would have to do manually
# Script always 1 file and do not need to be compiled , unlike programs
# API's tend to use scripts
# Scripting languages designed to be easy to understand and very sequantial - rapid development and use
# Scripts use less or no abstraction and are not as flexible as programs. But they are much easier to read and write.
# Scripts always used to fulfill a specific task, programs do many things
# Scripts are almost always written in 'high level languages' (easy to read) - Python, Bash,  Ruby.

# Why Python?
# Open source
# Many libraries (allow us to do things in few lines)
# Easy to understand
# Large community (often times script we want is already written)
# Language interoperability (can talk to other languages, OS's and software) e.g. using python to allow C to talk to other C derived languages

# Why is Scripting important for DevOps engineers
# Automation -> Of mundane tasks
# Can check certificate expiry dates
# Can automate crud process
# can automate ip fetching etc
# Scripts are ran in the terminal - write <python file_name>
# Scripts generally use modules and libraries to be as efficient as possible
# 7 Core modules in Python
# Sys -lets us interact with python environment
# Os - lets us interact with our operating system -file and folder manipulation
# Subprocesses - lets us create and interact with subprocesses being managed by our python interpreter
# Math
# Random
# DateTime
# JSON

# Sys module scripts
import sys

print(sys.version)

# OS module script

print(os.getcwd()) # get current working directory

#os.chdir("C:\Users\benux\PycharmProjects") #can change working directory

print(os.getcwd())

# os.mkdir("path") # Make a directory

# Subprocess module script
import subprocess

subprocess.run(["python", "hello_world.py"]) # Before automating make sure its not an infinite loop

# Math module scripts
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

#Random module scripts
import random

randum = random.randrange(1, 10)
print(randum)

# DateTime module scripts
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module script # human readable language that is used to transfer data between systems
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x) # change python data into json

print(y) # Prints x in json format
