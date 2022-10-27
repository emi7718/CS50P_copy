expression = input('Enter both integers and the operand: ')
x , y , z = expression.split()

x = int(x)
z = int(z)

if y == '+':
    print(float(x + z))
elif y == '/':
    print(float(x / z))
elif y == '*':
    print(float(x * z))
else:
     print(float(x - z))


