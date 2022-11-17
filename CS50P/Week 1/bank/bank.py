x = input("Enter Greeting: ").strip().lower()

if x.startswith("hello") == True:
    print("$0")
elif x.startswith("h") == True:
    print("$20")
else:
    print("$100")