import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv("../.env")

PRODUCT_URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
HEADER = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6'
}
MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
SENT_TO = os.getenv("SENT_TO")
TARGET_PRICE = 100


def get_html():
    response = requests.get(url=PRODUCT_URL, headers=HEADER)
    response.raise_for_status()
    return response.text


def parse_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    a_price_whole = soup.find(name='span', class_='a-price-whole').getText()
    a_price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
    product_title = soup.find(name='span', id='productTitle').getText().strip()

    return float(f'{a_price_whole}{a_price_fraction}'), product_title


def smtp_handler(product_title, product_price):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = MY_EMAIL
        msg["To"] = SENT_TO
        msg["Subject"] = "Amazon Price Alert!"

        # Email body with UTF-8 encoding
        body = f"{product_title} is now {product_price}\n\n{PRODUCT_URL}"
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(MY_EMAIL, SENT_TO, msg.as_string())

        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == '__main__':
    some_html = get_html()
    price, title = parse_data(some_html)
    if price < TARGET_PRICE:
        smtp_handler(title, price)
