import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Code for web scraping from cardekho.com 
def check_prices():
    url = "https://www.cardekho.com/"
    car_model = "maruti-suzuki-swift" 

    response = requests.get(f"{url}{car_model}.htm")
    soup = BeautifulSoup(response.content, 'html.parser')

    car_prices = [int(price.text.replace('Rs.', '').replace(',', '').strip()) for price in soup.find_all('div', class_='pricevalue')]

    threshold_price = int(threshold_entry.get())

    for price in car_prices:
        if price < threshold_price:
            toaster = ToastNotifier()
            toaster.show_toast("Car Price Alert", f"The price of the {car_model} has dropped below Rs. {threshold_price}!", duration=10)
