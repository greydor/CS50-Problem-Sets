# define list dictionary
list = {}

while True:

    # end loop and output list if user input = ctrl + d
    try:
        item = input().lower()
    except EOFError:
        for i in sorted(list):
            print(list[i], i.upper())
        break

    # check if item is in list
    # increment item qty if existing, add to list otherwise
    if item in list:
        list[item] = list[item] + 1
    else:
        list[item] = 1