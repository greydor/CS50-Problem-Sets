import sys

def main():
    if len(sys.argv) != 2 or sys.argv[1].endswith(".py") == False:
        sys.exit("error")
    else:
        print(sys.argv[1])
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        line = line.lstrip()
        if line.startswith("#"):
            pass
        elif line:
            count = count + 1

    print(count)






if __name__ == "__main__":
    main ()