networks = ["BTC", "LTC", "DASH", "ZEC", "DOGE"] # підтримувані монети
BASE_URL = "https://sochain.com/api/v2/" # API URL
# функція для розрахунку ціни

def calculate_price(data):

    prices = [float(entity["price"]) for entity in data["data"]["prices"]]

    return f"{(sum(prices) / len(prices)):.4f} USD"