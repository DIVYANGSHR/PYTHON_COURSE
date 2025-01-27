#globle function 
# x=100


# def show():
#     x=200
#     z=globals()['x']
#     print("this is me ", x)
#     print("this is me z:" , z)

# show()

# print("this is he" , x)


def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        
        return n * factorial(n - 1)

n=5
print(f'factorial of {n} is : {factorial(n)}')

print()



