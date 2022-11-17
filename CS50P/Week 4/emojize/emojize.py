import emoji

def main():

# Promt user for input
    x = input("Enter Input: ")

# Add text to user input
    x2 = "Output: " + x

# Look up and print emoji
    print(emoji.emojize(x2))











if __name__ == "__main__":
    main()