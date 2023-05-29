from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

end = False
while not end:
    user = input(f"What would you life? {menu.get_items()}: ").lower()
    if user == "off":
        end = True
    elif user == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(user)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)