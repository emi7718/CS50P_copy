groceries_list = {}
while True:
    try:
        grocery_item = input().upper()
        if grocery_item in groceries_list:
            groceries_list.update({grocery_item : groceries_list[grocery_item] + 1})
        else:
            groceries_list.update({grocery_item : 1})
    except EOFError:
        break
for i in sorted(groceries_list):
    print(groceries_list[i], i)
