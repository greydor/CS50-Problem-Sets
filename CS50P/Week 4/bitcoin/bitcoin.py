import requests
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        buy_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Enter a number")
    else:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = data.json()
        price = data["bpi"]["USD"]["rate_float"] * buy_amount

        print(f"${price:,.4f}")











if __name__ == "__main__":
    main()