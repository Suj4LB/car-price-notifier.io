import sqlite3
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import Tk, Label, Entry, Button, messagebox


def check_prices():
    
    conn = sqlite3.connect('car_prices.db')
    cursor = conn.cursor()
    
    threshold_price = int(threshold_entry.get())

    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()

    for car in cars:
        car = car[1:]
        make, model, price = car
        if price < threshold_price:
            print(f"The price of a {make} {model} has dropped below Rs.{threshold_price}!")
    conn.close()

# GUI Setup
root = Tk()
root.title("Car Price Notifier")

label_threshold = Label(root, text="Threshold Price (in Rs. ):")
label_threshold.pack(pady=5)

threshold_entry = Entry(root)
threshold_entry.pack(pady=5)

check_button = Button(root, text="Check Prices", command=check_prices)
check_button.pack(pady=10)

root.mainloop()
