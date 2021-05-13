import requests
from bs4 import BeautifulSoup
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

URL = "https://store.nba.com/los-angeles-lakers/mens-los-angeles-lakers-kobe-bryant-mitchell-and-ness-gold-1996-97-hardwood-classics-authentic-player-jersey/t-36368591+p-0340583648494+z-9-3598894427?_ref=p-SRP:m-GRID:i-r0c0:po-0"

headers={
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find("div", class_="product-title-container").get_text()
price = soup.find("span", class_="regular-price").get_text()
if int(price[-6: -3]) < 500 :
    account_sid = 'AC462903e14452bac2be328a2fb5460dab'
    auth_token = '34460e45b0594d295522db2a68fad3f3'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Price Dropped Hurry!!!!",
                        from_='xxxxxxxx',
                        to='xxxxxxxx'
                    )

    print(message.sid)



