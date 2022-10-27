menu = {'Baja Taco': 4.00,
        'Burrito': 7.50,
        'Bowl': 8.50,
        'Nachos': 11.00,
        'Quesadilla': 8.50,
        'Super Burrito': 8.50,
        'Super Quesadilla': 9.50,
        'Taco': 3.00,
        'Tortilla Salad': 8.00
        }
total = float()
while True:
    try:
        print('Item: ', end = '')
        menu_item = menu[input().title()]
        total = total + menu_item
        print('Total: ${:.2f}'.format(total))
    except KeyError:
        pass
    except EOFError:
        break
