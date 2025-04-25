#Weekly Task 07
#reads a text file and outputs the number of e's it contains
#should take the filename from an argument on the command line

import sys
import os

#using sys.argv to insure filename was provided
if len(sys.argv) < 2: 
    print("Error: Please provide a filename as a command-line argument.")
    sys.exit(1)

filename = sys.argv[1]

#checking if the file exists
if not os.path.isfile(filename):
    print("Error: The file '{}' does not exist.".format(filename))
    sys.exit(1)

#reading the file and counting all the e's in the file
try:
    with open(filename, 'r') as f: 
        data = f.read()
        count = data.lower().count("e") 
        print(count)
except Exception as e: #using try/except to handle errors (e.g. no perm to read file)
    print("An error occurred while reading the file: {}".format(e))