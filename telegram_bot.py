import requests
from config import BOT_TOKEN, CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{8618348040:AAHVdRVjKBgFaSb7t3JGt2BKh-IVX_yVFj4}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
