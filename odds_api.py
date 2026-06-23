import requests
from config import ODDS_API_KEY

def get_odds():
    url = f"https://api.the-odds-api.com/v4/sports/soccer/odds/?apiKey={b9a18f45e75e6d369e5b824f18196af2}&regions=eu&markets=h2h,totals&oddsFormat=decimal"
    return requests.get(url).json()
