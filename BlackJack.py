# Black jack game

#import Modules
import random
from art import BlackJack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#functions 
def deal_card():
    return random.choice(cards)

def calculate_score(card_name):
  """sum all value in list """
  if sum(card_name)==21 and len(card_name)==2:
    return 0 
  if 11 in card_name and sum(card_name) > 21:
    card_name.remove(11)
    card_name.append(1)
  x = sum(card_name)
  return x


def detect_blkjk(usr_total, comp_total):
  if usr_total == comp_total:
    return "It's a Draw"
  elif usr_total == 0:
    return "You Win with a BlackJack"
  elif comp_total == 0:
    return "You lose, computer has a BlackJack"
  elif usr_total > 21:
    return "You lose, you went over"
  elif comp_total > 21:
    return "You win, comp went over"
  elif usr_total > comp_total:
    return "You win"
  else:
    return "You lose"  
####
def play_game():
  print(BlackJack)
  user_cards = []
  comp_cards = []

  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())
  # for first_draw in range(2):
  #     user_cards.append (random.choice(cards))
  #     comp_cards.append (random.choice(cards))
  # print(f"user = {user_cards}")
  # print(f"computer = {comp_cards}")

  while not is_game_over:
    # usr_total = 0 
    # for t in user_cards:
    #   usr_total += t
    # comp_total = 0 
    # for t in comp_cards:
    #   comp_total += t
    usr_total = calculate_score(user_cards)
    comp_total = calculate_score(comp_cards)

    print (f"Your cards: {user_cards}, current score is {usr_total}")
    print (f"Computer's first card is {comp_cards[0]}")

  #  detect_blkjk()

    if usr_total == 21 or comp_total == 21 or usr_total > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while comp_total != 0 and comp_total < 17:
    comp_cards.append(deal_card())
    comp_total = calculate_score(comp_cards)

  print(f"  Your final hand is {user_cards}, your score is {usr_total}")
  print(f"   Comp fnal hand is {comp_cards}, score is {comp_total}")
  print(detect_blkjk(usr_total, comp_total))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
  play_game() 