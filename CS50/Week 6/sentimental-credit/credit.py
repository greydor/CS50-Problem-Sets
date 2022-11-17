sum = 0
x = 0
i = 0

card = int(input("Number: "))

while i <= 16:

    num = int(card / (10**i))
    if num == 0:
        break

    y = x
    x = num % 10

    if i % 2 == 0:
        sum += x
    else:
        if x * 2 >= 10:
            tens_digit = int(x * 2 / 10)
            ones_digit = x * 2 % 10
            sum += ones_digit + tens_digit
        else:
            sum += x * 2

    starting = 10 * x + y
    remainder = sum % 10
    i += 1

if remainder == 0:
    # Check for Visa card.
    if (i == 13 or i == 16) and x == 4:
        print("VISA")
    # Check for Amex card.
    elif i == 15 and (starting == 34 or starting == 37):
        print("AMEX")
    # Check for Mastercard card.
    elif i == 16 and (
        starting == 51
        or starting == 52
        or starting == 53
        or starting == 54
        or starting == 55
    ):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
