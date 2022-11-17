import csv
from tabulate import tabulate
import sys

def main():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    menu = []

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)

    print(tabulate(menu, headers=" firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()