# Homework 2 Part I (quiz_part1.py)
# Coder: Zonglin Han
# This program simulates single question.

# Print the question and the options
print('''ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso''')

answer = input('Enter your choice:')    # get user input
if answer == 'a':   # correct answer
    print('Correct!')
else:               # wrong answer
    print('The correct answer was a')