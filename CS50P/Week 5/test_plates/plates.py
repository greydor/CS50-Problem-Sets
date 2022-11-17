def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_length(s) == False:
        return False
    elif start_with_letters(s) == False:
        return False
    elif number_check(s) == False:
        return False
    elif only_alphanumeric(s) == False:
        return False
    else:
        return True

def start_with_letters(x):
    if x[0:1].isnumeric():
        return False
    else:
        return True

def check_length(x):
    if 2 <= len(x) <= 6:
        return True
    else:
        return False

def number_check(x):
    num_count = 0
    for i in x:
        if i == "0" and num_count == 0:
            return False
        elif i.isnumeric():
            num_count = num_count + 1
        elif num_count > 0:
            return False
    return True

def only_alphanumeric(x):
    if x.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
