#Define the menu of restaurant
menu = {
    'Pizza':150,
    'Salad':100,
    'Burger':99,
    'Cold Coffee':80,
    'Biryani':200,
    'Masala Dosa':50,
    'Idli' : 40,
}

#Greet
print("Welcome to My Restaurant")
print(" Pizza: Rs150\n Salad: Rs100\n Burger: Rs99\n Cold Coffee: Rs80\n Biryani:Rs200\n Masala Dosa: Rs50\n Idli:Rs40\n ")

order_total = 0
# 80 + 99 =179

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1] #0 + 150
    print(f"Your item {item_1} has been added to your order") 

else:
    print(f"Ordered item {item_1} is not avaialable yet !")

another_order = input("DO you  want to add another item ? (Yes/No)")
if another_order == "Yes":
    item_2 = input ("Enter the name of second order =")
    if item_2 in menu:
        order_total += menu [item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")

another_order = input("DO you  want to add another item ? (Yes/No)")
if another_order == "Yes":
    item_3 = input ("Enter the name of second order =")
    if item_3 in menu:
        order_total += menu [item_2]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"Ordered item {item_3} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")

print(f" Thanku for order wait 10-15 minutes ")

