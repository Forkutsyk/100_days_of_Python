import smtplib
import datetime as dt
import random


# smtp.mail.yahoo.com

my_email = "oleksandr.poplavskiy14@gmail.com"
password = "kbgacnrytttbafcn"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    with open("quotes.txt", 'r') as quotes:
        quotes_list = quotes.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="oleksandrpoplavskyi@yahoo.com",
            msg=f"Subject:quote\n\n{random.choice(quotes_list)}")
        connection.close()
