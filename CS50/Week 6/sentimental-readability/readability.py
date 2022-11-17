def main():

    text = input("Enter text: ")

    sentences = count_sentences(text)

    letters = count_letters(text)

    words = count_words(text)

    index = readability_index(sentences, words, letters)

    if index < 1:
        print("Before Grade 1")
    elif 1 <= index <= 15:
        print(f"Grade {index}")
    elif index >= 16:
        print("Grade 16+")


def count_sentences(text):
    sentences = 0
    for char in text:
        if char == "." or char == "?" or char == "!":
            sentences += 1
    return sentences


def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = 1
    for char in text:
        if char == " ":
            words += 1
    return words


def readability_index(sentences, words, letters):
    S = sentences / (words / 100)
    L = letters / (words / 100)
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index


main()
