# Import data
from coffee_data import MENU, resources, logo
import sys

turn_off = False
resources['money'] = 0
to_be_continued = True
# functions

# Process coins.
def get_coins():
    """Ask the user to insert coins and sum it """
    print("Please insert coins.")
    quarter = 0.25 * float(input("how many quarters?: "))
    dime = 0.10 * float(input("how many dimes?: "))
    nickle = 0.05 * float(input("how many nickles?: "))
    penny = 0.01 * float(input("how many pennies?: "))
    total = quarter + dime + nickle + penny
    return total


# Check transaction successful?
def successful_transaction(user_paid, selected_coffee):
    """Check that the user has inserted enough money to purchase the drink they selected."""
    coffee_cost = MENU[selected_coffee]['cost']
    if user_paid >= coffee_cost:
        balance = round(user_paid - coffee_cost, 2)
        resources['money'] += coffee_cost
        print (f"Here is 💲{balance} dollars in change.💵 \n Here is your ☕️ {selected_coffee}. Enjoy!")
    else:
        print (f"Sorry that's not enough money. Money refunded.")


# Check resources sufficient?
def check_resource_availablity(selected_coffee):
    """Check enough Milk, Water & Coffee are available"""
    global to_be_continued
    selected_resource = MENU[selected_coffee]['ingredients']
    for key in selected_resource:
        if resources[key] >= selected_resource[key]:
            resources[key] -= selected_resource[key]
        else:
            to_be_continued = False
            print (f"Sorry there is not enough {key}.")
            # break
            

def main():
    check_resource_availablity(user_selection)
    if to_be_continued:
        user_paid = get_coins()
        successful_transaction(user_paid, user_selection)



# Turn off the Coffee Machine by entering “off” to the prompt

# Ask user what they want
while not turn_off:

    print (logo)

    user_selection = input("    What would you like? (espresso/latte/cappuccino): ")

    # TODO 2. Print report
    if user_selection == "report":
        for key, value in resources.items():
            print(key, ' : ', value)
    elif user_selection == 'off':
        turn_off = True
        print(" 🙏🏼 Thank you, Good Bye!")
    else:
        main()  # Make Coffee.


