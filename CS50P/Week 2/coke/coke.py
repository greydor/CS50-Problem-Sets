due = 50
print("Amount Due:", due)
while True:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        coin = 0
    if due <= 0:
        due = -1 * due
        print("Change Owed:",due)
        break
    print("Amount Due:", due)