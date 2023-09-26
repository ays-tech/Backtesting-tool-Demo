# File: visualization.py

import matplotlib.pyplot as plt
import pandas as pd

# Function to create basic equity curve plot
def plot_equity_curve(portfolio_value):
    try:
        # Create a time index based on the number of data points
        time_index = range(len(portfolio_value))
        
        # Plot the equity curve
        plt.figure(figsize=(10, 6))
        plt.plot(time_index, portfolio_value, label='Equity Curve', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Portfolio Value')
        plt.title('Basic Equity Curve')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    # Load historical forex data (to be replaced with actual data retrieval)
    forex_data = pd.read_csv("historical_forex_data.csv")
    
    # Define a trading strategy (to be generated in earlier steps)
    strategy = "A simple moving average strategy"
    
    # Perform backtesting and get results (to be implemented in Step 5)
    total_return, max_drawdown = perform_backtest(strategy, forex_data)
    
    if total_return is not None:
        print(f"Total Return: {total_return:.2f}%")
        print(f"Max Drawdown: {max_drawdown:.2f}%")
        
        # Generate portfolio value over time (replace with actual portfolio values)
        portfolio_value = [100000]  # Example initial capital
        
        # Create an equity curve plot
        plot_equity_curve(portfolio_value)
