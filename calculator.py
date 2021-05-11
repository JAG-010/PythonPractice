# Calculator
from art import calc
# print (logo)
# Add
def add (n1, n2):
  return n1 + n2

#Subtract
def sub (n1, n2):
  return n1 - n2

# Multiply
def mult (n1, n2):
  return n1 * n2

# Divide
def div (n1, n2):
  return n1 / n2


math = {"+": add,
        "-": sub,
        "*": mult,
        "/": div}

def Calculator():
  print(calc)
  num1 = int(input("What is the first number? "))

  for n in math:
    print (n)

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is the next number? "))
    answer = math[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_selection = input(f"Press 'y' to continue with {answer} \n 'n' to start over \n 'x' to exit: ")
    if user_selection == 'y':
      num1 = answer
    elif user_selection == 'x':
      should_continue = False
      print("Good Bye")
    else:
      should_continue = False
      Calculator()

Calculator()