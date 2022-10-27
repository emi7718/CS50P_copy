my_string = input('Input: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in my_string:
    for vow in vowels:
        if char == vow:
            my_string = my_string.replace(char, '')

print('Output:', my_string)
