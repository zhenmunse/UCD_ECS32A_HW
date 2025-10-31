# Homework 4 Part V (translate.py)
# Coder: Zonglin Han
# This program runs a Pig Latin translator.

raw_input = input("Enter a word:").lower() # Prompt user for a word

if raw_input[0] in "aeiou": # Check if the first letter is a vowel
    pig_latin = raw_input + "way"   # Form Pig Latin for vowel-starting words
else: # If the first letter is a consonant
    pig_latin = raw_input[1:] + raw_input[0] + "ay" # Form Pig Latin for consonant-starting words
print(f"{raw_input} in Pig latin is {pig_latin}") # Print the Pig Latin translation