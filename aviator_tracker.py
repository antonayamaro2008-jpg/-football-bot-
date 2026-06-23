from telegram_bot import send_message

# 👉 resultados de exemplo (depois mudamos para automático)
results = [1.2, 1.5, 3.0, 1.1, 2.2, 1.3, 1.8, 4.5, 1.0, 1.6]

def analyze(results):

    avg = sum(results) / len(results)
    low = len([x for x in results if x < 2])
    very_low = len([x for x in results if x < 1.5])

    risk = 0

    if avg < 2:
        risk += 30
    if low >= 6:
        risk += 40
    if very_low >= 4:
        risk += 30

    msg = f"""
⚠️ AVIATOR TRACKER

📊 Média: {round(avg,2)}x
📉 <2x: {low}/10
📉 <1.5x: {very_low}/10

🔥 Risk Score: {risk}/100
"""

    send_message(msg)


analyze(results)
