#!/usr/bin/env python3 
import twint
import requests
import smtplib
from email.message import EmailMessage
from datetime import date, datetime, timedelta

#Get some tweets 
search = "cardano"
date = datetime.today()
since = date.strftime("%Y-%m-%d")
#yesterday = date.today() - timedelta(days=1)
#since = yesterday.strftime("%Y-%m-%d")
tweets = []
bodyTweets = ""

c = twint.Config()
c.Search = search
c.Verified = True
c.Since = since
c.Store_object = True
c.Store_object_tweets_list = tweets

twint.run.Search(c)


#Get cardano Price
Cardanowebsite = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
r = requests.get(Cardanowebsite)
result = r.json()
price = result.get('cardano', {}).get('usd')

bodyTweets = "Cardano Price: " + str(price) + "\n \n \n"

#make tweets a pretty string for email body
for t in tweets:
    t.tweet = t.tweet.replace("http://","LinkBanned")
    t.tweet = t.tweet.replace("https://","LinkBanned")
    t.tweet = t.tweet.replace(".com","LinkBanned")
    t.tweet = t.tweet.replace(".net","LinkBanned")
    bodyTweets = bodyTweets + t.username + " | " + t.name + " \n" + t.tweet + "\n \n" 

        
#Get cardano Price
Cardanowebsite = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
r = requests.get(Cardanowebsite)
result = r.json()
price = result.get('cardano', {}).get('usd')

#Email configuration
sender = "email@email.com"
reciever = "email@email.com"
password = "password"
msg_body = bodyTweets

#send email
msg = EmailMessage()
msg['subject'] = 'Cardano Report - Price: ' + str(price)   
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,password)
    smtp.send_message(msg)