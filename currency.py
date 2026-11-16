import requests
answer = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
data = answer.json()
currency = input("Введите валюту(н.р USD, EUR):").upper()
if currency in data["Valute"]: 
    Value = data["Valute"][currency]["Value"]
    Nominal = data["Valute"][currency]["Nominal"]
    price = Value / Nominal
    print(f"Цена {currency} = {price} руб.")
else:
    print("Такой валюты нет")