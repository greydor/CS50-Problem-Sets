word = input("Enter Input: ")
word_snake = ""
for x in word:
    if x.isupper():
        x = "_" + x.lower()
    word_snake = word_snake + x
print(word_snake)
