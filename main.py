import requests
from bs4 import BeautifulSoup
import smtplib
from colorama import *
init()
import time

# Define the URL to scrape (example: AutoTrader)
url = "https://www.autotrader.com/cars-for-sale/"

# Define your price threshold
threshold_price = 20000  # Replace with your desired threshold

# Send a request to the website and get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract car prices (assuming prices are in USD)
car_prices = [int(price.text.replace('$', '').replace(',', '')) for price in soup.find_all('span', class_='item-price')]

# Check if any car's price is below the threshold
for price in car_prices:
    if price < threshold_price:
        # Send an email notification
        smtp_server = 'your_smtp_server.com'  # Replace with your SMTP server
        smtp_port = 587  # Replace with your SMTP port
        sender_email = 'your_email@gmail.com'  # Replace with your email
        sender_password = 'your_password'  # Replace with your email password
        receiver_email = 'receiver_email@gmail.com'  # Replace with the recipient's email

        subject = 'Car Price Alert'
        body = f'The price of a car has dropped below ${threshold_price}!'

        message = f'Subject: {subject}\n\n{body}'

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)
                print("Email notification sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
