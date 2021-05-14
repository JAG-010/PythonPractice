# Guess the number game

import random
from art import GuessTheNumber
print(GuessTheNumber)
# name = input('Hello, What is your name? ')
print('Welcome to number gussing game!\n I am thinking of a number from 1 to 100, can you find it? ')
somenumber = random.randint(1, 100)
difficulty_level = input("Choose a difficulty. Type 'easy' or hard: ")

if difficulty_level == 'easy':
    # run easy level
    no_of_attempts = 10
else:
    #run hard level
    no_of_attempts = 5
# print ('Hint:'+str(somenumber))
to_continue = True
while to_continue:
    if no_of_attempts < 1:
        print("You ran out of attempts")
        to_continue = False
    else:
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
        usr_choice = int(input("Make a guess: "))

        if usr_choice > somenumber:
            print("Too high")
            no_of_attempts -= 1
        elif usr_choice < somenumber:
            print("Too low")
            no_of_attempts -= 1
        else:
            to_continue = False
            print(f"You got it! The answer was {somenumber}")