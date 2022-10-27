
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_index = int()
    #check for lenght between 2 and 6
    if not (6 >= len(s) >=2):
        return False
    #exit if any character is not alphanumeric
    if not s.isalnum():
        return False
    if s.isalpha():
        return True
    for i in range(len(s)):
        if s[i].isnumeric():
            num_index = i
            break
    if num_index < 2:
        return False
    else:
        second_string = s[num_index:]
        if second_string[0] == '0':
            return False
        return second_string.isnumeric()




if __name__ == '__main__':
    main()

    