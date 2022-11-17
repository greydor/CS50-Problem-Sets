def main():
    x = input("Enter Greeting: ")
    print(f"${value(x)}")

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()

