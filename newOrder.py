import newMenu
order = dict()
pizza_list = list()
quantity_list = list()
amount_list = list()
pizza_name = ""
all_orders=list()

def getOrder(order_id):
    global pizza_name
    print()
    pizza_name=input("Enter Pizza Name: ")
    quantity=int(input("Enter number of "+pizza_name+": "))
    quantity_res = checkQuantity(pizza_name,quantity)
    if(quantity_res == 1):   
        for i in newMenu.menu:
            if(newMenu.menu[i]["pizza_name"]==pizza_name):
                cost_of_required_pizza = newMenu.menu[i]["cost_per_pizza"]
                break
        amount = quantity * cost_of_required_pizza
        order = createOrder(order_id, pizza_name, quantity, amount)
        updateMenu(pizza_name, quantity)
        return order
    return 0

def createOrder(order_id, pizza_name, quantity, amount):
    global order, pizza_list, quantity_list, amount_list
    pizza_list.append(pizza_name)
    quantity_list.append(quantity)
    amount_list.append(amount)
    order[order_id]={"pizza_name":pizza_list, "quantity":quantity_list, "amount":amount_list}
    return order

def checkQuantity(pizza_name,quantity):
    for i in newMenu.menu:
        if(newMenu.menu[i]["pizza_name"]==pizza_name):
            available_quantity = newMenu.menu[i]["quantity"]
            break
    if(quantity>available_quantity):
        return 0
    else:
        return 1
    
def updateMenu(pizza_name, quantity ):
    for i in newMenu.menu:
        if(pizza_name==newMenu.menu[i]["pizza_name"]):
            newMenu.menu[i]["quantity"]-=quantity

def displayOrder(order_id):
    global order, pizza_name, amount, quantity, total_price
    print()
    print(str("Order ID:"+str(order_id)).center(168,"-"),"\n")
    total_price = 0
    for i in range(1, len(order[order_id]["amount"])+1):
        total_price += order[order_id]["amount"][i-1]
        lst = ["Item no:", i, "Pizza Name:", order[order_id]["pizza_name"][i-1],"Quantity:", order[order_id]["quantity"][i-1],"Amount:", order[order_id]["amount"][i-1]]
        print("{: >30} {: >7} {: >20} {: >20} {: >15} {: >5} {: >20} {: >7}".format(*lst))
    print()
    print("{: >100} {: >10}".format("Total Amount:", "₹ "+str(total_price)))
    disc, total_price = calcDiscount(total_price)
    print("{: >100} {: >10}".format("Discount: ", str(disc)+"%"))
    print("{: >100} {: >10}".format("Total Amount after Discount:", "₹ "+str(total_price)))
    print("----".center(168,"-"))

def addToMainOrder(Order, total_price):
    global all_orders
    all_orders += [[total_price, Order]]

#not complete
def displayAllOrders():
    global all_orders
    all_orders = sortOrdersDesc(all_orders)
    print()
    print("ORDERS".center(168,"-"),"\n\n")
    for ls in all_orders:
        temp_dic = ls[1]
        temp_total_price = ls[0]
        for order_id in temp_dic:
            print("Order ID:", order_id)
            pizza_list = temp_dic[order_id]["pizza_name"]
            quantity_list = temp_dic[order_id]["quantity"]
            amount_list = temp_dic[order_id]["amount"]
            for i in range(len(pizza_list)):
                print("Pizza Name: "+str(pizza_list[i]), "Quantity Ordered: "+str(quantity_list[i]), "Total: "+str(amount_list[i]), sep = "\t\t")
        print("Total Amount Paid =", temp_total_price, "\n\n")
    print("----".center(168,"-"))

def sortOrdersDesc(all_orders):
    all_orders.sort(key= lambda x: x[0], reverse=True)
    return all_orders

def calcDiscount(total_price): 
    if(total_price<=500):
        total_price = total_price * 0.98
        discount = 2
    elif(total_price>500 and total_price<=1000):
        total_price = total_price * 0.95
        discount = 5
    elif(total_price>1000 and total_price<=5000):
        total_price = total_price * 0.9
        discount = 10
    else:
        total_price = total_price * 0.8
        discount = 20

    return discount, total_price