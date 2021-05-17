from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mi = MenuItem()
m = Menu()
cm = CoffeeMaker()

print(m.get_items())
# print(m.find_drink("latte"))

print(cm.report())
