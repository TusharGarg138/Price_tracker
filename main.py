import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

#my_email = os.environ["my_email"]
#my_pass = os.environ["my_pass"]

URL = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

