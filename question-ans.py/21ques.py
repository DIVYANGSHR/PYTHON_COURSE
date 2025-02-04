class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Woof!
