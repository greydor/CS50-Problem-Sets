x = input("Input: ")
x2 = ""

for i in x:
    lower = i.lower()
    if lower != "a" and lower != "e" and lower != "i" and lower != "o" and lower != "u":
        x2 = x2 + i

print(x2)