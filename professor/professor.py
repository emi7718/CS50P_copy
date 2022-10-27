from random import randint
'''
#here i had problems hard to figure out, I made a mistake
#in 37 uusing 1 instead of 0, and on line 57, leaving de counter sum inside of th if statement, it goes outside
#this were the errors i had:
:) professor.py exists
:) Little Professor rejects level of 0
:) Little Professor rejects level of 4
:) Little Professor rejects level of one
:) Little Professor accepts valid level
:( At Level 1, Little Professor generates addition problems using 0–9
    Did not find "6 + 6 =" in "Level: 7 + 7 =..."

:) professor.py exists
:) Little Professor rejects level of 0
:) Little Professor rejects level of 4
:) Little Professor rejects level of "one"
:) Little Professor accepts valid level
:) At Level 1, Little Professor generates addition problems using 0–9
:) At Level 2, Little Professor generates addition problems using 10–99
:) At Level 3, Little Professor generates addition problems using 100–999
:) Little Professor generates 10 problems before exiting
:( Little Professor displays number of problems correct
    Did not find "9" in "Level: 6 + 6 =..."
:) Little Professor displays EEE when answer is incorrect
:) Little Professor shows solution after 3 incorrect attempts
'''


def test_uni_case(x, y):
    counter = 1
    while counter <= 3:
        try:
            z = int(input(f'{x} + {y} = '))
        except ValueError:
            print('EEE')
            counter += 1
        else:
            if z == x + y:
                return True
            else:
                counter += 1
                print('EEE')
    print(f'{x} + {y} = {x + y}')
    return False


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError

def main():
    score = 0
    i = 1
    a = int()
    b = int()
    w = get_level()

    while i <= 10:
        a = generate_integer(w)
        b = generate_integer(w)
        if (test_uni_case(a, b)):
            score += 1
        i += 1
    print(f'Score: {score}')


if __name__ == '__main__':
    main()