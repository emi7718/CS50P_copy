def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check for lenght between 2 and 6
    if not (6 >= len(s) >=2):
        return False
    #exit if any character is not alphanumeric
    for char in s:
        if not char.isalnum():
            return False

    listed_string = list(s)

    #check if two first characters are letters
    for i in range(2):
        if listed_string[i].isnumeric():
            return False

    first_string = str()
    second_string = str()
    for char in s:
        if char.isalpha():
            first_string = first_string + char
        else:
            break
    second_string = s.replace(first_string,'')
    if len(second_string) != 0:
        for char in second_string:
            if char.isalpha():
                return False
        if second_string[0] == '0':
            return False
    return True

if __name__ == '__main__':
    main()
