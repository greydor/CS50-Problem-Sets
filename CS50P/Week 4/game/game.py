import sys
from random import randint

def main():
    output = ""
    while True:
        try:
            max_number = int(input("Level: "))
        except ValueError:
            pass
        else:
            if max_number > 0:
                true_value = randint(1,max_number)
                break
    while True:
        try:
             guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > 0:
                output = evaluate_guess(true_value, guess)
                if output ==  "Just right!":
                    print(output)
                    break
                else:
                    print(output)

# Compare guess to generated value
def evaluate_guess(t,g):
    if g == t:
        return "Just right!"
    if g > t:
        return "Too large!"
    if g < t:
        return "Too small!"

if __name__ == "__main__":
    main()