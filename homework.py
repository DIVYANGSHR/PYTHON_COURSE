def replace_char(s, curr_char, new_char):
    if curr_char in s:
        
        s = s.replace(curr_char, new_char)
    
    return s

test_cases = [
    ("hello,world,pyhton,python", "l", "s"),
    ("hello,world,pyhton,python", "w", "ax"),
    ("hello,world,pyhton,python", "p", "a")
]

for s, curr_char, new_char in test_cases:
    result = replace_char(s, curr_char, new_char)
    print(f"Original string: {s}")
    print(f"Replaced string: {result}")
    print('-' * 50)
