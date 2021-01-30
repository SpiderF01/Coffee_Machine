import collections

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}


# Function to print resource report
def print_report():
    for key in resources:
        print(f"{key.title()}: {resources[key]}{units[key]}")
    print(f"Money: ${format(profit, '.2f')}")


# Function to display price of drink selected
def display_price(drink):
    price = MENU[drink]["cost"]
    formatted_price = format(price, '.2f')
    return f"{drink.title()} price: ${formatted_price}"


# Function to count money entered into machine
def count_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


# Function to format money to 2 decimal points
def formatted_money(amount, desc):
    formatted_value = format(amount, '.2f')
    if desc == "money_entered":
        return f"Entered ${formatted_value}"
    elif desc == "change_given":
        return f"Change returned ${formatted_value}"
    else:
        return f"Money returned ${formatted_value}"


profit = 0

machine_on = True
while machine_on:
    # Function to check if enough resources for drink
    def check_resources(drink):
        if MENU[drink]["ingredients"]["water"] <= resources["water"]:
            if MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[drink]["ingredients"]["coffee"] <= resources["coffee"]:
                    return True
        else:
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
            if MENU[drink]["ingredients"]["milk"] == 0:
                pass
            elif MENU[drink]["ingredients"]["milk"] > resources["water"]:
                print("Sorry there is not enough milk")
            if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")


    drink_choice = input("What would you like? Espresso/Latte/Cappuccino: ").lower()

    # Turn off machine and quit while loop
    if drink_choice == "off":
        machine_on = False

    # Print report of resources
    elif drink_choice == "report":
        print_report()

    # Display drink price and money entered. Calculate change from money entered and cost of drink
    elif drink_choice == "espresso" or drink_choice == "latte" or drink_choice == "cappuccino":
        if check_resources(drink_choice):
            print(display_price(drink_choice))
            money = count_money()
            print(formatted_money(money, "money_entered"))
            cost = MENU[drink_choice]["cost"]
            change = money - cost

            if money >= cost:
                profit += cost

                # Update resources dictionary after drink dispensed
                temp_resources = collections.Counter(resources)
                temp_MENU = collections.Counter(MENU[drink_choice]["ingredients"])
                result_resources = temp_resources - temp_MENU
                resources = (dict(result_resources))

                print(f"Here is your {drink_choice.title()}. Enjoy!")

                # Only give change if exact money not entered
                if money > cost:
                    print(formatted_money(change, "change_given"))

            # Display if not enough money entered
            else:
                print("Not enough money entered")
                print(formatted_money(money, ""))
