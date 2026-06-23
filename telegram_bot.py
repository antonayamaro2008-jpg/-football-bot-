import requests
from config import BOT_TOKEN, CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{8603081100:AAEMHrUrQA_W6Q_YderSYgQP0TUYtmmyKHo}/sendMessage"
    requests.post(url, data={"chat_id": 6689658340, "text": text})
