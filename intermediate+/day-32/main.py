import smtplib
import datetime as dt
import random

# gmail_email = EMAIL
# gmail_password = PASSWORD
# gmail_smtp = "smtp.gmail.com"
# outlook_email = EMAIL
# outlook_password = PASSWORD
# outlook_smtp = "smtp-mail.outlook.com"

# with smtplib.SMTP(outlook_smtp, port=587) as connection:
#     connection.starttls()
#     connection.login(user=outlook_email, password=outlook_password)
#     connection.sendmail(
#         from_addr=outlook_email,
#         to_addrs=gmail_email,
#         msg="Subject:Teszt\n\nPyhtonbol kuldtem :D"
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1994, month=12, day=7)
# print(date_of_birth)

# now = dt.datetime.now()
# day_of_week = now.weekday()
# if day_of_week == 5:
#     with open("quotes.txt") as data_file:
#         quotes = data_file.readlines()
#         random_quote = random.choice(quotes)
#     with smtplib.SMTP(outlook_smtp, port=587) as connection:
#         connection.starttls()
#         connection.login(user=outlook_email, password=outlook_password)
#         connection.sendmail(
#             from_addr=outlook_email,
#             to_addrs=gmail_email,
#             msg=f"Subject:Daily Motivational quote\n\n{random_quote}"
#         )
