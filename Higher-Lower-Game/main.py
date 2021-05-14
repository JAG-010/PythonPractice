# from game_data import data
from game_data import data
import random
from art import logo, vs 
# option_a = ""
# option_b = ""

# function to run the game
def game():
    score = 0
    winner = ""
    game_not_over = True
    
    while game_not_over:
        if score == 0:      # if score=0 then choose parameter for both options
            option_a = random.choice(data)
            option_b = random.choice(data)
        else:               # if scrore is high then choose parameter for option B alone
            option_b = random.choice(data)
            while option_a == option_b: #if previous command set's same value as option_a, then change option_b
                option_b = random.choice(data)

        # print(option_a)
        # print(option_b)
        print(logo)

        if score > 0:
            print(f"You're right! Current {score}: ")
        
        # Print first option (A)
        print (f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.")
        
        print (vs)
        # Print second option (B)
        print (f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.")
        user_choice = input("Who has more followers? Type 'A' or 'B': ")

        
        
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
            print(f"Sorry, that's wrong. Final score: {score} ")

# call game() function
game()
