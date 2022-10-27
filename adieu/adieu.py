import inflect

p = inflect.engine()
mylist= []


while True:
    try:
        mylist.append(input('Name: ').strip())
    except EOFError:
        break
print('Adieu, adieu, to ' + p.join(mylist))