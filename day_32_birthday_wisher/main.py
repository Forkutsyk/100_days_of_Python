# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas
import datetime as dt
from random import randint
import os
from dotenv import load_dotenv

TEMPLATE = '[NAME]'


class BirthdayWisher:
    def __init__(self):
        self.df = pandas.read_csv("birthdays.csv")
        self.data_dic = self.df.to_dict(orient="records")

        self.birthday_congrats = ""
        load_dotenv("../.env")
        self.my_email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_EMAIL_PASSWORD")

        self.now = dt.datetime.now()
        self.month = self.now.month
        self.day = self.now.day
        self.main_logic()

    def sent_mail(self, send_to):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=send_to,
                msg=f"Subject:Happy birthday !!!\n\n{self.birthday_congrats}")
            connection.close()

    def main_logic(self):
        for person in self.data_dic:
            if person['month'] == self.month and person['day'] == self.day:
                mail_format = f"letter_templates/letter_{randint(1,3)}.txt"
                with open(mail_format) as file:
                    mail_text = file.read()
                    self.birthday_congrats = mail_text.replace(TEMPLATE, person['name'])
                    self.sent_mail(person['email'])


if __name__ == '__main__':
    app = BirthdayWisher()
