l = [ 1, 2, 3, 4, 5]

def square (x):
    return x **2

y = list (map(square, l))
print(y)

# using lmbda fuction in map 

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)


# result_list = list(doubled_numbers)

result_list= list(map(lambda x: x * 2, numbers))

print(result_list)

print()
