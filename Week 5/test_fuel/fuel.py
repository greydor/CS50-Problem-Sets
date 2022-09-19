def main():
    while True:
        fraction = input("Enter Fraction: ")
        try:
            fuel = convert(fraction)
        except (ValueError, ZeroDivisionError):
            print("error")
        else:
            percent = gauge(fuel)
            print(percent)




def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x / y > 1:
        raise ValueError
    return round(x / y * 100)




def gauge(percentage):
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            elif 1 < percentage < 99:
                return f"{percentage}%"



if __name__ == "__main__":
    main()



