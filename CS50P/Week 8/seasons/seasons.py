from datetime import date
import sys
import inflect
import re

p = inflect.engine()


def main():
    print(minutes(input("Date of birth: ")))


def minutes(date_in):
    matches = re.search(r"^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$", date_in)
    if not matches:
        sys.exit("Invalid date")
    date_in = date.fromisoformat(date_in)
    days = date.today() - date_in
    matches_2 = re.search("^([0-9]+ )", str(days))
    if not matches_2:
        return "Zero minutes"
    minutes = int(matches_2.group(1))*24*60
    minutes = p.number_to_words(int(minutes), andword="")
    return minutes.capitalize() + " minutes"






if __name__ == "__main__":
    main()