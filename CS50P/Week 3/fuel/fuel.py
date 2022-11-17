while True:
    try:
        x,y = input("Enter Fraction: ").split("/")
        x = int(x)
        y = int(y)
        x / y
    except (ValueError, ZeroDivisionError) as error:
        pass
    else:
        fuel = round((x / y) * 100)
        if 0 <= fuel <= 1:
            print("E")
            break
        elif 99 <= fuel <= 100:
            print("F")
            break
        elif 1 < fuel < 99:
            print(fuel,"%", sep="")
            break
