def main():
    my_string = shorten(input('Input: '))
    print('Output:', my_string)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in word:
        for vow in vowels:
            if char == vow:
                word = word.replace(char, '')
    return word


if __name__ == '__main__':
    main()
