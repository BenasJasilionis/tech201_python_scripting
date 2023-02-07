import os

# 1. Create a directory

# Directory
directory = "test_dir"

# parent Directory

parent_dir = "C:/Users/benux"

# Path
path = os.path.join(parent_dir, directory) # lets us join parent dir with new dir

# Create the DIR
# os.mkdir(path)
# print("Directory '% s' created" % directory) # the % represents

# 2.  Make a file in the new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Write to the new file
with open(os.path.join(path, filename),"w") as file1: # w stands for write
    toFile = "Contents of my new file"
    file1.write(toFile)
print(f"File {filename} created in {directory} folder")
