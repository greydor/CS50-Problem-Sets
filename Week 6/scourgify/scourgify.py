import sys
import csv

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")


    data_2 = []

    with open(sys.argv[1], "r", newline='') as file:
        data = csv.DictReader(file)
        for row in data:
            house = row["house"]
            last, first = row["name"].split(", ")
            row_2 = {"first":first, "last":last, "house":house}
            data_2.append(row_2)

    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data_2:
            writer.writerow(row)




if __name__ == "__main__":
    main()