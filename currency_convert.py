import requests

def currency_converter(amount,from_currency,to_currency):
    url=f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response=requests.get(url)
        data=response.json()
        conversion_rate=data['rates'][to_currency]
        converted_amount=amount*conversion_rate
        return converted_amount
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")
        return None

amount=int(input("enter your amount to convert to usd:"))
from_currency= input("Enter from currency (e.g., USD, INR): ").upper()
to_currency=input("Enter to currency (e.g., EUR, GBP): ").upper()

converted_amount=currency_converter(amount,from_currency,to_currency)

if converted_amount is not None:
    print(f"{amount}{from_currency}is equal to {converted_amount}{to_currency}")
