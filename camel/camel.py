my_string = input('please enter a string in camelcase format: ')
converted_string = str()
for char in my_string:
    if char.islower():
        converted_string = converted_string + char
    elif char.isupper():
        converted_string = converted_string + '_'
        char = char.lower()
        converted_string = converted_string + char
print(converted_string)