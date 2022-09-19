def main():
    word = input("Enter word: ")
    word = shorten(word)
    print(word)


def shorten(word):
    vowels = "AEIOUaeiou"
    for i in vowels:
        word = word.replace(i, "")

    return word


if __name__ == "__main__":
    main()