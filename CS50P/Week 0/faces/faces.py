def main():
    str1 = input("Enter Input: ")
    str1 = convert(str1)
    print(str1)

def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")

main()