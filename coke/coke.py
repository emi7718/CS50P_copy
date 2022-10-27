total = 0
amount_due = 50
coin = int()

while total < 50:
    print('Amount due: ', amount_due)
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5 and total < 50:
        total = total + coin
        amount_due = amount_due - coin
print('Change owed: ', total - 50)
