import requests
from telegram_bot import send_message
from config import ODDS_API_KEY

print("🧠 A analisar forma das equipas...")

url = f"https://api.the-odds-api.com/v4/sports/soccer/odds/?apiKey={ODDS_API_KEY}&regions=eu&markets=totals&oddsFormat=decimal"

response = requests.get(url)

if response.status_code != 200:
    print("Erro na API:", response.text)
    exit()

games = response.json()

MAX_ALERTS = 3
sent = 0

def format_market(outcome):
    name = outcome["name"]
    point = outcome.get("point")
    if point is not None:
        return f"{name} {point}"
    return name


def fake_team_form(team):
    """
    ⚠️ versão base (sem API estatística ainda)
    Vamos simular forma inicial baseada em heurística
    """
    return {
        "attack": 1.4,   # golos marcados médios
        "defense": 1.2   # golos sofridos médios
    }


for game in games:

    if sent >= MAX_ALERTS:
        break

    if "bookmakers" not in game:
        continue

    try:
        outcomes = game["bookmakers"][0]["markets"][0]["outcomes"]
    except:
        continue

    over = None
    under = None

    for o in outcomes:
        if "Over" in o["name"]:
            over = o
        if "Under" in o["name"]:
            under = o

    if not over or not under:
        continue

    home = fake_team_form(game["home_team"])
    away = fake_team_form(game["away_team"])

    # 🧠 estimativa de golos do jogo
    expected_goals = home["attack"] + away["attack"]

    over_odds = over["price"]
    under_odds = under["price"]

    over_prob = 1 / over_odds
    under_prob = 1 / under_odds

    score = 0
    pick = None
    odds = 0
    prob = 0

    # 🔥 lógica baseada em forma
    if expected_goals >= 2.5 and over_prob > 0.48:
        score += 40
        pick = format_market(over)
        odds = over_odds
        prob = over_prob

    if expected_goals < 2.5 and under_prob > 0.48:
        score += 40
        pick = format_market(under)
        odds = under_odds
        prob = under_prob

    if not pick:
        continue

    value = (prob * odds) - 1
    if value > 0.05:
        score += 25

    if 1.60 <= odds <= 2.10:
        score += 20

    if score < 75:
        continue

    confidence = min(5, max(1, score // 20))

    send_message(f"""🔥 OPORTUNIDADE BASEADA EM FORMA

⚽ {game['home_team']} vs {game['away_team']}

➡ Mercado: {pick}
📊 Odd: {odds}
📈 Probabilidade: {round(prob*100)}%

📊 Expected Goals: {round(expected_goals,2)}

⭐ Confiança: {confidence}/5
📊 Score: {score}/100

⚠️ Sistema Forma v1 (base)
""")

    sent += 1
