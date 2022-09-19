from pyfiglet import Figlet
from random import choice
import sys
figlet = Figlet()

def main():

    if len(sys.argv) == 1:

        # Selects a random font
        output_font = random_font()
        figlet.setFont(font=output_font)


    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":

        # Exit program if chosen font is not valid
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        # Selects a specified font
        figlet.setFont(font=sys.argv[2])

    else:
       sys.exit("Invalid usage")

    s = input("Input: ")
    print("Output: ",figlet.renderText(s), sep="\n")



# Choose a random font
def random_font():
    font = choice(figlet.getFonts())
    return font








main()