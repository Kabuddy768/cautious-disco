import requests
import json

# Set the Alpha Vantage API key
API_KEY = "YOUR_API_KEY"

# Define the function to get historical currency data from Alpha Vantage
def get_historical_currency_data(from_currency, to_currency, interval="daily"):
  """Gets historical currency data from Alpha Vantage.

  Args:
    from_currency: The currency to convert from.
    to_currency: The currency to convert to.
    interval: The interval of the data to get (daily, weekly, or monthly).

  Returns:
    A list of dictionaries, where each dictionary contains the following keys:
      date: The date of the data.
      open: The opening price of the currency pair.
      high: The highest price of the currency pair during the day.
      low: The lowest price of the currency pair during the day.
      close: The closing price of the currency pair.
  """

  url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={from_currency}&to_symbol={to_currency}&interval={interval}&apikey={API_KEY}"
  response = requests.get(url)
  data = json.loads(response.content)

  historical_data = []
  for date, values in data["Time Series FX (Daily)"].items():
    historical_data.append({
      "date": date,
      "open": values["1. open"],
      "high": values["2. high"],
      "low": values["3. low"],
      "close": values["4. close"]
    })

  return historical_data

# Get the USD/KES historical data
historical_data = get_historical_currency_data("USD", "KES")

# Print the historical data
for row in historical_data:
  print(row)
