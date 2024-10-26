#todo: 2. check resources sufficient to make drink order.

menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
      "cost": 1.5,
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 30,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 200,
            "coffee": 10,
        },
        "cost":1.5,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 500,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("sorry there is not enough {item}.")
            return False
    return True

def process_choice():
    print("please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def is_transaction_succesful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money.money refunds")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your drink {drink_name}.enjoy")
is_on = True


while True:
    choice = input(" what Would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
      print(f"water: {resources['water']}ml")
      print(f"milk: {resources['milk']}ml")
      print("coffee: {resources['coffee']}g")
      print(f"money ${profit}")
    else:
      drink = menu[choice]
      if is_resource_sufficient(drink["ingredients"]):
          payment = process_choice()
          if is_transaction_succesful(payment,drink["cost"]):
              make_coffee(choice,drink["ingredients"])