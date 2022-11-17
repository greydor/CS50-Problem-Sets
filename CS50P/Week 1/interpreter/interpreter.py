x,o,y = input("Enter Equation: ").split(" ")
x=float(x)
y=float(y)

if o == "+":
    print(x+y)
elif o == "-":
    print(x-y)
elif o == "*":
    print(x*y)
elif o == "/":
    print(round(x/y,1))