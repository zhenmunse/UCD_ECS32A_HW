# Homework 2 Part IV (quiz_part4.py)
# Coder: Zonglin Han
# This program simulates several questions, one genius question and tracks the score.

score = 0  # initialize score variable

def multipleChoice(question, options, answer): # define a function to handle multiple choice questions, ignore repeat of code
    print(question)
    for option in options:  # print all options
        print(option)
    user_answer = input('Enter your choice:') # get user input
    if user_answer == answer:   # correct answer
        print('Correct!')
        global score; score += 1  # increment score for correct answer
    else:                       # wrong answer
        print(f'The correct answer was {answer}')

# Call the function for each question
multipleChoice("ART: Who painted 'The Persistance of Memory'?", ['a. Dali', 'b. Munch', 'c. Picasso'], 'a')
multipleChoice('ENTERTAINMENT: How many oscars did Hitchcock win?', ['a. None', 'b. One', 'c. Two'], 'a')
multipleChoice('SCIENCE: Which dinosaur is most closely related to the pelican?', ['a. Velociraptor', 'b. Stegosaurus', 'c. Pterodactyl'], 'a')
multipleChoice('HISTORY: Which of the following was not invented in Baja California?', ['a. Margaritas', 'b. Chocolate', 'c. Caesar Salad'], 'b')
multipleChoice('SCIENCE AND NATURE: Can pigs swim?', ['a. Yes', 'b. No', 'c. Only in salt water'], 'a')
multipleChoice('SPORT AND LEISURE: What color is the middle Olympic ring?', ['a. Red', 'b. Blue', 'c. Black'], 'c')

print(f'Your total score is {score}')  # print the total score

print('GENIUS: In ancient Rome, what is L divided by X?') # genius question
geniusAnswer = input('Enter your answer:')
if geniusAnswer in ['V', '5']:  # correct answer
    print('Correct!')
else:   # wrong answer
    print('Correct answers were 5 or V')