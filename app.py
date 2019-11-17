import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/MOSISO-Mirrorless-Shockproof-Adjustable-Compatible/dp/B07797XJ8X/ref"
                       "=sr_1_1_sspa?crid=1RDR1BPJV0BIH&keywords=dslr+camera+bag&qid=1573955774&sprefix=dslr%2Caps"
                       "%2C154&sr=8-1-spons&psc=1&spLa"
                       "=ZW5jcnlwdGVkUXVhbGlmaWVyPUFONDAzSlRINVJBQlcmZW5jcnlwdGVkSWQ9QTA4MzQ5NTAyRjI5N1IzUjdaUVZHJmVuY3J5cHRlZEFkSWQ9QTA1NTAyNTczVldNTzYwMUk2OVpLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price priceBlockBuyingPriceString"})

string_price = element.text.strip()
price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 200:
    print("You Should buy the product!")
    print("The current price is {}".format(string_price))
else:
    print("Do not buy, its too expensive!")
# <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$29.99</span>
