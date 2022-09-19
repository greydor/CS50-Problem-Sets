import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search("^([0-9][0-9]?):?((?:[0-9][0-9])?) (A|P)M to ([0-9][0-9]?):?((?:[0-9][0-9])?) (A|P)M", s)
    if matches == None:
        raise ValueError

    start_hour = int(matches.group(1))
    start_min = matches.group(2)
    start_AM_PM = matches.group(3)
    end_hour = int(matches.group(4))
    end_min = matches.group(5)
    end_AM_PM = matches.group(6)

    if start_hour > 12 or end_hour > 12:
        raise ValueError
    if start_hour == 12 and start_AM_PM == "A":
        start_hour = 0
    if end_hour == 12 and end_AM_PM == "A":
        end_hour = 0
    if start_AM_PM == "P":
        if start_hour != 12:
            start_hour += 12
    if end_AM_PM == "P":
        if end_hour != 12:
            end_hour += 12
    if not start_min:
        start_min = "00"
    elif int(start_min) > 59:
        raise ValueError
    if not end_min:
        end_min = "00"
    elif int(end_min) > 59:
        raise ValueError

    start_hour = f"{start_hour:02}"
    end_hour = f"{end_hour:02}"


    return f"{start_hour}:{start_min} to {end_hour}:{end_min}"




if __name__ == "__main__":
    main()
