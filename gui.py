import tkinter as tk
from tkinter import filedialog
import pandas as pd
import threading
from backtest_engine import perform_backtest, SimpleMovingAverageStrategy

sample_data = []

def process_data(data, short_window_entry, long_window_entry):
    try:
        # Get the contents of the Entry widgets
        short_window_text = short_window_entry.get()
        long_window_text = long_window_entry.get()

        # Validate the input (check if they are valid integers)
        if short_window_text.isdigit() and long_window_text.isdigit():
            # Convert the validated input to integers
            short_window = int(short_window_text)
            long_window = int(long_window_text)

            # Initialize the strategy with moving average window parameters
            strategy = SimpleMovingAverageStrategy(short_window, long_window)

            # Perform backtesting with the strategy
            total_return, max_drawdown, winning_percentage = perform_backtest(data, [strategy])

            # Display the results (you can update the GUI to show these results)
            print("Total Return:", total_return)
            print("Max Drawdown:", max_drawdown)
            print("Winning Percentage:", winning_percentage)
        else:
            print("Invalid input: Short and long windows must be valid integers.")
    except Exception as e:
        print("Error during data processing:", str(e))


def browse_file_data_collection():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path)
            sample_data.extend(data.values.tolist())

            # Start processing data in the background thread
            background_thread = threading.Thread(target=process_data, args=(data, short_window, long_window))
            background_thread.start()
        except Exception as e:
            print("Error during file loading:", str(e))
def start_backtest():
    print("Starting backtest...")
    if 'loaded_data' in globals() and loaded_data is not None:
        try:
            short_window = int(short_window_entry.get())
            long_window = int(long_window_entry.get())
            strategy = SimpleMovingAverageStrategy(short_window, long_window)
            total_return, max_drawdown, winning_percentage = perform_backtest(loaded_data, [strategy])
            print("Total Return:", total_return)
            print("Max Drawdown:", max_drawdown)
            print("Winning Percentage:", winning_percentage)
        except Exception as e:
            print("Error during backtesting:", str(e))
    else:
        print("No data loaded for backtesting.")

window = tk.Tk()
window.title("Data Collection and Backtesting")

data_collection_frame = tk.Frame(window)
data_collection_frame.pack(padx=20, pady=20)

data_collection_label = tk.Label(data_collection_frame, text="Data Collection")
data_collection_label.pack()
data_collection_button = tk.Button(data_collection_frame, text="Browse CSV File", command=browse_file_data_collection)
data_collection_button.pack()

backtest_frame = tk.Frame(window)
backtest_frame.pack(padx=20, pady=20)

# Create labels and entry fields for backtesting parameters
short_window_label = tk.Label(backtest_frame, text="Short MA Window:")
short_window_label.pack()
short_window = tk.Entry(backtest_frame)
short_window.pack()

long_window_label = tk.Label(backtest_frame, text="Long MA Window:")
long_window_label.pack()
long_window = tk.Entry(backtest_frame)
long_window.pack()


start_backtest_button = tk.Button(backtest_frame, text="Start Backtest", command=start_backtest)
start_backtest_button.pack()

window.mainloop()
