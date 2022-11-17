while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        pass
    else:
        if 1 <= height <= 8:
            break
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(i):
        print("#", end="")
    print("  ", end="")
    for j in range(i):
        print("#", end="")
    print()
