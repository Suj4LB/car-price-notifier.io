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
            
# GUI Setup
root = tk.Tk()
root.title("Car Price Notifier")

style = ThemedStyle(root)
style.set_theme("plastik")

frame = ttk.Frame(root, padding="30")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter Threshold Price (in INR):")
label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)

threshold_entry = ttk.Entry(frame)
threshold_entry.grid(row=1, column=0, pady=(0, 10))

check_button = ttk.Button(frame, text="Check Prices", command=check_prices)
check_button.grid(row=2, column=0, pady=(0, 10))

root.mainloop()
