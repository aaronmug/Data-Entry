from pprint import pprint

import requests
from bs4 import BeautifulSoup

from form import Form

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=ZILLOW_URL)
response.raise_for_status()
# pprint(response.text)

soup = BeautifulSoup(response.text, features="html.parser")
# pprint(soup)

image_cards = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

image_links = [image_card.select_one(selector='a').get('href') for image_card in image_cards]

prices = []

addresses = []

for image_card in image_cards:
    price = image_card.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").getText()
    if "+" in price:
        prices.append(price.split("+")[0])
    elif "/" in price:
        prices.append(price.split("/")[0])

for image_card in image_cards:
    address = image_card.find(name="address").getText().strip()
    if " | " in address:
        new_address = address.replace(" | ", "")
        addresses.append(new_address)
    else:
        addresses.append(address)

form_upload = Form()
for i in range(len(addresses)):
    form_upload.input_info(address=addresses[i], price=prices[i], link=image_links[i])
