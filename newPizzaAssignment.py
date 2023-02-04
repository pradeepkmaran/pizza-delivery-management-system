import newMenu
import newOrder

newMenu.getDetailsInitial()

while(True):
    print()
    new_order = input("Add New Order? ")
    print()

    if(new_order == "No"):
        newMenu.printUpdatedMenu(newMenu.menu)
        break

    order_id = int(input("Enter order ID: "))
    print()
    number_of_pizza = int(input("Enter Types of Pizza to order: "))
    temp_number_of_pizza = number_of_pizza
    newOrder.order={}
    newOrder.pizza_list = []
    newOrder.quantity_list = []
    newOrder.amount_list = []

    while(temp_number_of_pizza>0):
        temp_number_of_pizza -= 1
        main_order = newOrder.getOrder(order_id)

        if(main_order == 0):
            print("\nSorry for the inconvenience. The pizza you requested is out of stock.")
            print("Only", newMenu.findQuantity(newOrder.pizza_name), "pizzas are available in the type you selected.")
            unavailable_reply = input("\nWould you like to choose some other Pizza? ")

            if(unavailable_reply == "Yes"):
                temp_number_of_pizza += 1
            else:
                main_order = newOrder.order

    newOrder.displayOrder(order_id)
    newOrder.addToMainOrder(newOrder.order, newOrder.total_price)
    print()
    newMenu.printUpdatedMenu(newMenu.menu)

newOrder.displayAllOrders()

    