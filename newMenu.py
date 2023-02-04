def getDetailsInitial():
    n = int(input("Enter the types of Pizzas in Menu: "))
    global menu
    menu = dict()
    for i in range(n):
        print()
        product_id = int(input("Enter Pizza ID: "))   
        pizza_name = input("Enter Pizza Name: ")
        cost_per_pizza = int(input("Enter Cost per Pizza: "))
        quantity = int(input("Enter number of Pizzas available: "))
        menu[product_id] = {"pizza_name":pizza_name, "cost_per_pizza":cost_per_pizza, "quantity":quantity}
    printMenu(menu)

def printMenu(menu):
    global pizza_name, cost_per_pizza, quantity
    print()
    print("MENU".center(168,"-"))
    for i in menu:
        lst = ["Pizza ID:", i, "Name:", menu[i]["pizza_name"],"Cost:", menu[i]["cost_per_pizza"]]
        print("{: >50} {: >7} {: >20} {: >20} {: >20} {: >7}".format(*lst))
    print()
    print("----".center(168,"-"))

def printUpdatedMenu(menu):
    global pizza_name, cost_per_pizza, quantity
    print()
    print("MENU".center(168,"-"))
    for i in menu:
        lst = ["Pizza ID:", i, "Pizza Name:", menu[i]["pizza_name"],"Cost:", menu[i]["cost_per_pizza"],"Quanitity Left:",menu[i]["quantity"]]
        print("{: >30} {: >7} {: >20} {: >25} {: >15} {: >7} {: >20} {: >7}".format(*lst))
    print()
    print("----".center(168,"-"))

def findQuantity(pizza_name):
    global menu
    for i in menu:
        if(menu[i]["pizza_name"] == pizza_name):
            return menu[i]["quantity"]
