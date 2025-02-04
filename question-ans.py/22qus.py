class Animal:
    def speak(self):
        return "Animal speaks"

class Cat(Animal):  # Cat overrides speak method from Animal
    def speak(self):
        return "meows!"

cat = Cat()
print(cat.speak())  # Output: meows!
