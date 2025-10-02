# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300,
    "AMZN": 3500
}

print("📊 Stock Portfolio Tracker")
portfolio = {}
total_investment = 0

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Available:", ", ".join(stock_prices.keys()))
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
print("\n💰 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: save to file
save = input("\nDo you want to save the summary to portfolio.txt? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("----------------------\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("✅ Portfolio saved to portfolio.txt")
