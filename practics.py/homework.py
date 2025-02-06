# def replace_char(s, curr_char, new_char):
#     if curr_char in s:
        
#         s = s.replace(curr_char, new_char)
    
#     return s

# test_cases = [
#     ("hello,world,pyhton,python", "l", "s"),
#     ("hello,world,pyhton,python", "w", "ax"),
#     ("hello,world,pyhton,python", "p", "a")
# ]

# for s, curr_char, new_char in test_cases:
#     result = replace_char(s, curr_char, new_char)
#     print(f"Original string: {s}")
#     print(f"Replaced string: {result}")
#     print('-' * 50)


# ----  find odds no ====

# n = 10
# sum_odds = 0
# for i in range(1, n+1):
#     if i % 2 : 
#         print(i) 
#         sum_odds += i
# print(sum_odds)

# Function  factorial
# n = 5
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result

# print(factorial(n))


# # Prompt the user to enter a number
# number = float(input("Enter a number: "))

# # C if the number is positive
# if number > 0:
#     print("The number is positive.")
# #  if the number is zero
# elif number == 0:
#     print("The number is zero.")
# # If the number is not positive or zero, then it is negative
# else:
#     print("The number is negative.")




# # Define a list of fruits
# fruits = ["apple", "banana", "cherry"]

# # Use a for loop to iterate through the list
# for fruit in fruits:
#     print(fruit)

# # Initialize a counter variable
# counter = 1

# # Use a while loop to repeat until the counter reaches 5
# while counter <= 5:
#     print(counter)
#     counter += 1  # Increment the counter


# # Define a function named greet
# def greet():
#     print("Hello, World!")

# # Call the function
# greet()


# # Define a class named Person
# class Person:
#     # The __init__ method initializes the object's attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Define a method to display the person's details
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Create an object of the Person class
# person1 = Person("Alice", 30)

# # Call the display method
# person1.display()

# # Define a class named Animal
# class Animal:
#     # The __init__ method initializes the object's attributes
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     # Define a method to display the animal's details
#     def display(self):
#         print(f"Name: {self.name}, Species: {self.species}")

# # Create an object of the Animal class
# animal1 = Animal("Leo", "Lion")

# # Call the display method
# animal1.display()



# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         return "Woof!"
# my_dog = Dog("Buddy", "Golden Retriever")
# print(my_dog.name)  # Outputs: Buddy
# print(my_dog.breed) # Outputs: Golden Retriever
# print(my_dog.bark()) # Outputs: Woof!


# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# # Creating an object from the Car class
# my_car = Car("Thar", "mahindra")

# print(my_car.make) 
# print(my_car.model) 

class Product:
    def __init__(self, id):
        self.id = id
        
    def product_details(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_product(self):
        print(f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

p = Product(id=1)
p.product_details(name="laptop", price=100000, quantity=2)
p.display_product()
