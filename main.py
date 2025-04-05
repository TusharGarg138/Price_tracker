import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

#my_email = os.environ["my_email"]
#my_pass = os.environ["my_pass"]

URL = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# ====================== Add Headers to the Request ===========================
#header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
#      "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response  = requests.get(URL)
data = response.text
#print(data)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())
price = soup.find(class_="a-offscreen").get_text()

price_without_dollar = price.split("$")[1]

price_as_float = float(price_without_dollar)
#print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
#print(title)

buy_price = 100

# ====================== Send the email ===========================

if price_as_float < buy_price:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ['SMTP_add'], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["my_email"], os.environ["my_pass"])
        connection.sendmail(
           from_addr=os.environ["my_email"],
            to_addrs=os.environ["my_email"],
            msg=f"Subject: Amazon price alert \n\n {message}:\n {URL}".encode("utf-8"))

