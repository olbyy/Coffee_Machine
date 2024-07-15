from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

while True:
    choice = input("What would you like espresso/latte/cappuccino?: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        money_machine.process_coins()
        if choice == latte.name and money_machine.make_payment(latte):
            coffee_maker.make_coffee(latte)
        elif choice == espresso.name:
            coffee_maker.make_coffee(espresso)
        elif choice == cappuccino.name:
            coffee_maker.make_coffee(cappuccino)
