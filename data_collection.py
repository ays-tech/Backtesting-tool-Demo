import tkinter as tk
from tkinter import filedialog
import pandas as pd
import threading

# Function to process data in the background
def process_data(data, currency_pair):
    # Simulate processing by printing the first few rows and the associated currency pair
    print(f"Processing data for {currency_pair}...")
    print(data.head())

# Function to handle the "Browse" button click
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        currency_pair = currency_entry.get()  # Get currency pair from user input
        data = pd.read_csv(file_path)
        
        # Start processing data in the background thread
        background_thread = threading.Thread(target=process_data, args=(data, currency_pair))
        background_thread.start()

# Create the GUI window
window = tk.Tk()
window.title("Data Collection")

# Create an input field for the currency pair
currency_label = tk.Label(window, text="Enter Currency Pair:")
currency_label.pack()
currency_entry = tk.Entry(window)
currency_entry.pack()

# Create a button to browse for the CSV file
browse_button = tk.Button(window, text="Browse CSV File", command=browse_file)
browse_button.pack(padx=20, pady=20)

# Start the GUI main loop
window.mainloop()
