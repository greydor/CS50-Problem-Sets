import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        rand_1 = generate_integer(level)
        rand_2 = generate_integer(level)
        solution = rand_1 + rand_2
        print(f"{rand_1} + {rand_2} = ")

        for i in range(4):
            if i == 3:
                print(f"{rand_1} + {rand_2} = {solution}")
                break
            try:
                answer = int(input("Enter Answer: "))
            except ValueError:
                print("EEE")
            else:
                if answer == solution:
                    score = score + 1
                    break
                else:
                    print("EEE")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Enter Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
