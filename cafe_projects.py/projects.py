# Define the menu of the restaurant
menu = {
    'Pizza': 150,
    'Salad': 100,
    'Burger': 99,
    'Cold Coffee': 80,
    'Biryani': 200,
    'Masala Dosa': 50,
    'Idli': 40,
}

# Function to add an item to the menu
def add_item(menu, item, price):
    if item in menu:
        print(f"{item} is already in the menu.")
    else:
        menu[item] = price
        print(f"{item} has been added to the menu with a price of Rs{price}.")

# Function to update the price of an item in the menu
def update_item(menu, item, price):
    if item in menu:
        menu[item] = price
        print(f"The price of {item} has been updated to Rs{price}.")
    else:
        print(f"{item} is not in the menu.")

# Function to delete an item from the menu
def delete_item(menu, item):
    if item in menu:
        del menu[item]
        print(f"{item} has been removed from the menu.")
    else:
        print(f"{item} is not in the menu.")

# Greet the customer
print("Welcome to My Restaurant")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# Order items
while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available yet!")
    
    another_order = input("Do you want to add another item? (Yes/No) ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is Rs{order_total}")
print("Thank you for your order. Please wait 10-15 minutes.")

# Menu management
while True:
    action = input("Would you like to add, update, or delete an item from the menu? (Add/Update/Delete/Show/Exit) ").lower()
    if action == 'add':
        item = input("Enter the name of the item to add: ")
        price = int(input("Enter the price of the item: "))
        add_item(menu, item, price)
    elif action == 'update':
        item = input("Enter the name of the item to update: ")
        price = int(input("Enter the new price of the item: "))
        update_item(menu, item, price)
    elif action == 'delete':
        item = input("Enter the name of the item to delete: ")
        delete_item(menu, item)
    elif action=="show":
        for items, price in menu.items():
            print(f"Item: {items}, Price: {price}")

    elif action == 'exit':
        break
    else:
        print("Invalid action. Please choose Add, Update, Delete, or Exit.")

print("Updated menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
