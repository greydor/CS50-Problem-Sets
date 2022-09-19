def main():
    name_list = []
    count = 0

    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            break
        else:
            count = count + 1

    # Add "and" near end of names list
    try:
        if len(name_list) > 1:
            name_list[len(name_list) - 1] = "and " + name_list[len(name_list) - 1]
    except IndexError:
        print()
    else:
        try:
            print("\nAdieu, adieu, to " + generate_output(name_list))
        except TypeError:
            count = count - 1

# Create output string based on list of names
def generate_output(ls):
    output = ls[0]
    if len(ls) == 1:
        output = ls[0]
        pass
    else:
        for i in range(len(ls)):
            if i > 1:
                output = output + ", " + ls[i]

            #Add "!" temporarily to swap out later depending on how many names there are
            elif i == 1:
                output = output + "! " + ls[i]
    if len(ls) == 2:
        output = output.replace("!","")
    elif len(ls) > 2:
        output = output.replace("!",",")
    return output


    #print("Adieu, adieu, to ")



if __name__ == "__main__":
    main()