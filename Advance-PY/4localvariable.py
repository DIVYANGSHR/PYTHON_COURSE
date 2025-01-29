class MyClass:
    def __init__(self):
        self.instance_variable = "I am an instance logic variable"

    def my_method(self):
        
        local_variable = "I am a local unlogic variable"
        print(local_variable)

       
        print(self.instance_variable)


obj = MyClass()

obj.my_method()

print(obj.instance_variable)

# print(local_variable)