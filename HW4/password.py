# Homework 4 Part II (password.py)
# Coder: Zonglin Han
# This program validates a user's password input.

pwd = input("Enter password:") # Prompt user for password

# Check password criteria and print corresponding messages
if len(pwd) >= 8: print("Has length")
if any(c.islower() for c in pwd): print("Has lower case")
if any(c.isupper() for c in pwd): print("Has upper case")
if any(c.isdigit() for c in pwd): print("Has digit")
if any(c in "!@#$%&" for c in pwd): print("Has special")