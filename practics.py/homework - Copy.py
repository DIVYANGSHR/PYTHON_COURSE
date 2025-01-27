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
n = 5
def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(n))


