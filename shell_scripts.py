import os
import subprocess

# Python doesn't actually run shell commands
# Instead wwe can use Python to run shell script files

script_dir = os.path.dirname(__file__) # stores path to current file

script_absolute_path = os.path.join(script_dir ,"C:\Users\benux\PycharmProjects\tech201_python_scripting\tech201_python_scripting/script.sh", shell=True)

subprocess.call(['sh', script_absolute_path])