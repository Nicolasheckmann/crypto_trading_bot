import config
from binance.client import Client

client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY)

prices = client.get_all_tickers()

print(prices)