#!/usr/bin/env python3 
import json
import requests
import smtplib
from email.message import EmailMessage

# If you use GMail, you need to make a burner/service account for your sender and then allow "Less Secure app acecss" on that account. 

targetPrice = 1000
bottomPrice = 1.5

# Coingecko has a very cool API along with a url builder for simple gets 
Cardanowebsite = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
r = requests.get(Cardanowebsite)
result = r.json()
price = result.get('cardano', {}).get('usd')


if price >= targetPrice:
    sender = "Email@gmail.com"
    reciever = "Email@gmail.com"
    password = "P@sswr0d"
    msg_body = '''
        WOW!
        TO THE MOON!!!!
        '''
    # action
    msg = EmailMessage()
    msg['subject'] = 'Cardano Hit ' + str(price)   
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)


if price <= bottomPrice:
    sender = "Email@gmail.com"
    reciever = "Email@gmail.com"
    password = "P@sswr0d"
    msg_body = '''
        AHH!
        OH NO, ITS GOING TO ZERO!!!!
        AHHHHHHHHHHHHHH!
        
        Time to Buy!!!!!
        '''
    # action
    msg = EmailMessage()
    msg['subject'] = 'Cardano Hit ' + str(price)   
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)


print(price)
