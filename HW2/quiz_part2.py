# Homework 2 Part II (quiz_part2.py)
# Coder: Zonglin Han
# This program simulates several questions.

def singleQuestion(question, options, answer): # define a function to handle all questions, to ignore repeat of code
    print(question)
    for option in options:  # print all options
        print(option)
    user_answer = input('Enter your choice:') # get user input
    if user_answer == answer:   # correct answer
        print('Correct!')
    else:                       # wrong answer
        print(f'The correct answer was {answer}')

# Call the function for each question
singleQuestion("ART: Who painted 'The Persistance of Memory'?", ['a. Dali', 'b. Munch', 'c. Picasso'], 'a')
singleQuestion('ENTERTAINMENT: How many oscars did Hitchcock win?', ['a. None', 'b. One', 'c. Two'], 'a')
singleQuestion('SCIENCE: Which dinosaur is most closely related to the pelican?', ['a. Velociraptor', 'b. Stegosaurus', 'c. Pterodactyl'], 'a')
singleQuestion('HISTORY: Which of the following was not invented in Baja California?', ['a. Margaritas', 'b. Chocolate', 'c. Caesar Salad'], 'b')
singleQuestion('SCIENCE AND NATURE: Can pigs swim?', ['a. Yes', 'b. No', 'c. Only in salt water'], 'a')
singleQuestion('SPORT AND LEISURE: What color is the middle Olympic ring?', ['a. Red', 'b. Blue', 'c. Black'], 'c')