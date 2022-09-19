def main():
    x1 = input("Enter Time: ")
    x2 = convert(x1)
    if 7 <= x2 <= 8:
        print("breakfast time")
    elif 12 <= x2 <= 13:
        print("lunch time")
    elif 18 <= x2 <= 19:
        print("dinner time")



def convert(time):
    c = 0
    if time.endswith("pm"):
        time = time.strip(" pm")
        c = 1
    elif time.endswith("am"):
        time = time.strip(" am")

    h, m = time.split(":")
    h = float(h)
    if c == 1:
        h = h+12
    m = float(m)
    return h + m / 60

main()
