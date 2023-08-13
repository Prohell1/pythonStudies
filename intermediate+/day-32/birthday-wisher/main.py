import pandas
import datetime as dt
import smtplib
import random

outlook_email = EMAIL
outlook_password = PASSWORD
outlook_smtp = "smtp-mail.outlook.com"

with open("letters/letter_1.txt") as f:
    letter_1 = f.read()

with open("letters/letter_2.txt") as f:
    letter_2 = f.read()

with open("letters/letter_3.txt") as f:
    letter_3 = f.read()

letters = [letter_1, letter_2, letter_3]

df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for friend in birthdays:
    if friend["month"] == month and friend["day"] == day:
        chosen_letter = random.choice(letters)
        mail_to_send = chosen_letter.replace("[NAME]", friend["name"])
        with smtplib.SMTP(outlook_smtp, port=587) as connection:
            connection.starttls()
            connection.login(user=outlook_email, password=outlook_password)
            connection.sendmail(
                from_addr=outlook_email,
                to_addrs=friend["email"],
                msg=f"Subject:Happy Birthday!\n\n{mail_to_send}"
            )

