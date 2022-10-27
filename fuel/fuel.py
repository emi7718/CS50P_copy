while True:
    try:
        fraction = (input('Fraction: ').split('/'))
        if int(fraction[0]) <= int(fraction[1]):
            x = round(((int(fraction[0])/int(fraction[1])) * 100))
            break
    except (ValueError, ZeroDivisionError, IndexError, NameError):
        pass
if x <= 1:
    print('E')
elif x >= 99:
    print('F')
else:
    print(f'{x}%')
