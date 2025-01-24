# addition of num ===================

from functools import reduce
numbers = [1, 2, 3, 4, 5, 6 ,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sum_result = reduce(lambda x, y: x + y, numbers,)

print("Sum:", sum_result)

print()

