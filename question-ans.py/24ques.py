class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("John", 30)
print(person.get_name())  # Output: John
person.set_name("Doe")
print(person.get_name())  # Output: Doe
