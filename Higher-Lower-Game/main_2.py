# from game_data import data
from game_data import data
import random
from art import logo, vs 

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')


### xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ####
###   New Method
### xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ####
score = 0
option_a = ""
option_b = ""
game_not_over = True

def display_options(option_a, option_b, score):
    print(logo)
    if score > 0:
        print(f"You're right! Current {score}: ")
    print (f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print (f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.")

##
def game(user_choice):
    global score, game_not_over, option_a, option_b
    if option_a["follower_count"] > option_b["follower_count"]:
        winner = 'A'
    else:
        winner = 'B'

    if winner == user_choice:
        option_a = option_b
        print("WIN")
        score += 1
    else:
        game_not_over = False
        clear()
        print(f"Sorry, that's wrong. Final score: {score} ")

while game_not_over:
    if score == 0:      # if score=0 then choose parameter for both options
        option_a = random.choice(data)
        option_b = random.choice(data)
    else:               # if scrore is high then choose parameter for option B alone
        clear()
        option_b = random.choice(data)
        while option_a == option_b: #if previous command set's same value as option_a, then change option_b
            option_b = random.choice(data)
    
    display_options(option_a, option_b, score)
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    game(user_choice)

