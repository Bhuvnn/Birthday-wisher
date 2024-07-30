#Because of google security you can't access your account from here, so to resolve that u will have to generate an app password for it,
# for that simpy search google app passwords and login and generate app password

# For Email use the smtp.gmail.com
# For yahoo use smtp.yahoo.live.com
# for other mails, you can simply search for the smtp connection request for your mail

import datetime as dt
import pandas
import smtplib
import random

SENDER_EMAIL="Your email here"
MAIL_URL="smtp.gmail.com"
PROXY="Your mail URL proxy"

#setting Csv file
data=pandas.read_csv(r"____paste the path of csv file here____")
dict=data.to_dict(orient="records")

# #setting email
connection=smtplib.SMTP(MAIL_URL,PROXY)
connection.starttls()
connection.login(user="___Your Email here_____",password="______Your password____")

#setting date and time
date=dt.datetime.now()
current_day=date.day
current_month=date.month

# setting a birthday text file
number=random.randint(1,3)

for info in dict:
    month=info["month"]
    day=info["day"]
    if current_day==day and current_month==month:
        with open(rf"__paste the initial path here____\Birthday Email sender\letter_templates\letter_{number}.txt") as file:
            letter=file.read()
            new_letter=letter.replace("[NAME]",info["name"])
        connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=info["email"],msg=f"subject:Greetings \n\n{new_letter}")
        print("email sent")
connection.close()