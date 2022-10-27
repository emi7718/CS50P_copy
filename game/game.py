from random import randint

guess = int()
rand_num = int()
while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            rand_num = randint(1,level)
            break
    except ValueError:
        pass
while True:
    try:
        guess = int(input('Guess: '))
        if guess > 0:
            if guess < rand_num:
                print('Too small!')
            elif guess > rand_num:
                print('Too large!')
            else:
                print('Just Right!')
                break
    except ValueError:
        pass