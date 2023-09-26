import pandas as pd

class SimpleMovingAverageStrategy:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def get_signal(self, data, index):
        if index < self.long_window:
            return 0  # Not enough data to generate a signal

        short_ma = data['Close'].iloc[index - self.short_window : index].mean()
        long_ma = data['Close'].iloc[index - self.long_window : index].mean()

        if short_ma > long_ma:
            return 1  # Buy signal
        elif short_ma < long_ma:
            return -1  # Sell signal
        else:
            return 0  # No signal

def perform_backtest(data, strategies):
    # Initialize portfolio variables
    initial_balance = 100000  # Starting balance
    balance = initial_balance
    position = 0  # Number of shares/contracts held
    portfolio_value = []  # Store portfolio value at each time step
    max_portfolio_value = initial_balance

    # Risk management parameters
    risk_per_trade = 0.02  # Maximum risk per trade (2% of portfolio)
    stop_loss_percent = 0.05  # Maximum acceptable loss per trade (5%)

    # Performance metrics
    total_return = 0
    max_drawdown = 0
    winning_trades = 0
    losing_trades = 0
    total_trades = 0

    # Iterate through historical data
    for index, row in data.iterrows():
        # Apply multiple strategies
        for strategy in strategies:
            signal = strategy.get_signal(data, index)
            print(f"Date: {row['Date']}, Signal: {signal}, Balance: {balance}, Position: {position}")

            # Calculate position size based on risk per trade
            if signal == 1:
                risk_amount = balance * risk_per_trade
                stop_loss_price = row['Close'] * (1 - stop_loss_percent)
                position_size = int(risk_amount / (row['Close'] - stop_loss_price))
                position = position_size
                balance -= position_size * row['Close']

            # Sell signal
            elif signal == -1:
                balance += position * row['Close']
                position = 0

            # Calculate portfolio value
            current_portfolio_value = balance + position * row['Close']
            portfolio_value.append(current_portfolio_value)

            # Track maximum portfolio value
            max_portfolio_value = max(max_portfolio_value, current_portfolio_value)

            # Calculate trade results
            if signal == 1:
                total_trades += 1
            elif signal == -1:
                total_trades += 1
                trade_return = (current_portfolio_value - initial_balance) / initial_balance
                if trade_return > 0:
                    winning_trades += 1
                else:
                    losing_trades += 1

    # Calculate performance metrics
    total_return = (portfolio_value[-1] - initial_balance) / initial_balance
    max_drawdown = (max_portfolio_value - initial_balance) / initial_balance
    winning_percentage = (winning_trades / total_trades) * 100

    return total_return, max_drawdown, winning_percentage

# Example usage:
if __name__ == "__main__":
    # Load historical forex data (to be replaced with actual data retrieval)
    forex_data = pd.read_csv("historical_forex_data.csv")

    # Define backtesting parameters (e.g., moving average windows)
    short_window = 5
    long_window = 20

    # Create a strategy instance
    strategy = SimpleMovingAverageStrategy(short_window, long_window)

    # Perform backtesting with the strategy
    total_return, max_drawdown, winning_percentage = perform_backtest(forex_data, [strategy])

    if total_return is not None:
        print("Total Return:", total_return)
        print("Max Drawdown:", max_drawdown)
        print("Winning Percentage:", winning_percentage)
