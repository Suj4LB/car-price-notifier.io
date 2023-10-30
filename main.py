# Import necessary modules
import sqlite3  # For SQLite database operations
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
from win10toast import ToastNotifier  # For Windows toast notifications
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import Tk, Label, Entry, Button, messagebox

# Function to check car prices
def check_prices():
    # Connect to the SQLite database
    conn = sqlite3.connect('car_prices.db')
    cursor = conn.cursor()
    
    # Get the threshold price from the input field
    threshold_price = int(threshold_entry.get())

    # Retrieve data from the 'cars' table in the database
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()

    # Check each car's price against the threshold
    for car in cars:
        car = car[1:]
        make, model, price = car
        if price < threshold_price:
            # If the price is below the threshold, print a message and show a Windows toast notification
            print(f"The price of a {make} {model} has dropped below Rs.{threshold_price}!")
            notifier = ToastNotifier()
            notifier.show_toast(f"The Price of {make} {model} has dropped !", " ", duration=2)
    
    # Close the database connection
    conn.close()

# GUI Setup
root = Tk()
root.title("Car Price Notifier")

# Create a label for the threshold price
label_threshold = Label(root, text="Threshold Price (in Rs. ):")
label_threshold.pack(pady=5)

# Create an entry field for the threshold price
threshold_entry = Entry(root)
threshold_entry.pack(pady=5)

# Create a button to check prices and link it to the check_prices function
check_button = Button(root, text="Check Prices", command=check_prices)
check_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
