def main():
    print(gauge(convert(input('Fraction: ').strip())))


def convert(str_value):
    if not(str_value.index('/')):
        raise ValueError
    value_list = str_value.split('/')
    if not(value_list[0].isnumeric() and value_list[1].isnumeric()):
        raise ValueError
    x = int(value_list[0])
    y = int(value_list[1])

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return round((x / y) * 100)


def gauge(int_value):
    if int_value >= 99:
        return 'F'
    elif int_value <= 1:
        return 'E'
    else:
        return f'{int_value}%'


if __name__ == '__main__':
    main()
