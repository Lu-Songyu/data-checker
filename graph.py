from email.quoprimime import body_check
from poplib import POP3_SSL_PORT
from credential import credentials
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time
from instaloader import Instaloader, Profile

from credential import credentials

L = Instaloader()
 
PROFILE = "target-name"
profile = Profile.from_username(L.context, PROFILE)
# Login using the credentials
L.login(credentials.get('ins_username'),credentials.get('ins_password'))
posts = profile.get_posts()
 

time.sleep(10)
client = Client(credentials.get('twilio_sid'),credentials.get('twilio_token'))

body = "Here are their posts"


for post in posts:
    link = post.url
    message = client.messages.create(
        body=body,
        media_url=(link),
        from_=credentials.get('mynumber'),
        to=credentials.get('toNumber')
    )

