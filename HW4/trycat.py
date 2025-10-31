# Homework 4 Part VII (trycat.py)
# Coder: Zonglin Han
# This program simulates UNIX cat command with error handling.

while True:
    fileName = input("Enter a file name to open:") # Prompt user for file name
    try:
        with open(fileName, 'r') as file: # Open the file in read mode
            content = file.read() # Read the entire content of the file
            print(content, end="") # Print the content to the console
        break
    except FileNotFoundError:   # Handle file not found error
        print(f"Could not open '{fileName}'") # Print error message