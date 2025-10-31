# Homework 3 Part I (parrot.py)
# Coder: Zonglin Han
# This program simulates a noisy parrot.

while True:
    c = input(">")
    if c.lower() == "quiet":
        break
    print(c.upper())
