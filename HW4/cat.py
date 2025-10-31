# Homework 4 Part VI (cat.py)
# Coder: Zonglin Han
# This program simulates UNIX cat command.

fileName = input("Enter a file name to open:") # Prompt user for file name

with open(fileName, 'r') as file: # Open the file in read mode
    content = file.read() # Read the entire content of the file
    print(content, end="") # Print the content to the console