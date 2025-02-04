class Ex:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            return f"a: {a}, b: {b}"
        elif a is not None:
            return f"a: {a}"
        else:
            return "No arguments"

obj = Ex()
print(obj.display(1, 2))  # Output: a: 1, b: 2
print(obj.display(1))     # Output: a: 1
print(obj.display())      # Output: No arguments
