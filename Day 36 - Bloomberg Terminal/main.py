import requests
from twilio.rest import Client
# ---------------------------- API STOCKMARKET ------------------------------- #
params_stock_market = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "apikey",
}
response_stock_market = requests.get(url="https://www.alphavantage.co/query", params=params_stock_market)
response_stock_market.raise_for_status()
response_stock_market = response_stock_market.json()

# ---------------------------- DATE ------------------------------- #
data = response_stock_market["Time Series (Daily)"]
dates = sorted(data.keys(), reverse=True)
today_open = dates[0]
yesterday_close = dates[1]

today_open_price = float(data[dates[0]]["1. open"])
yesterday_close_price = float(data[dates[1]]["4. close"])


# ---------------------------- API NEWS ------------------------------- #

params_news = {
    "q": "Tesla",
    "from": yesterday_close,
    "to": today_open,
    "apiKey": "apikey"
}
response_news = requests.get(url="https://newsapi.org/v2/everything", params=params_news)
response_news.raise_for_status()
response_news = response_news.json()
# ---------------------------- NEWS PRINT FUNC ------------------------------- #
def news_print():
    n= 0
    for articles in response_news["articles"]:
        if n == 3:
            break
        name = articles["source"]["name"]
        title = articles["title"]
        url = articles["url"]
        spaces = "______________________________________________________________________________________"
        print(name)
        print(title)
        print(url)
        print(spaces)
        sms_body =(
            f"{params_stock_market['symbol']}: {arrow}{percent_change}\n"
            f"Headline: {title}")
        sms_send(sms_body)
        n += 1
# ---------------------------- SMS FUNC ------------------------------- #
def sms_send(body):
    account_sid = "account_sid"
    auth_token = "auth_token"
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to= "num",
        from_="num",
        body=body
    )

# ---------------------------- increase/decreases ------------------------------- #

percent_change = (today_open_price - yesterday_close_price) / yesterday_close_price * 100
arrow = "🔺" if percent_change > 0 else "🔻"

if percent_change >= 5:
    news_print()
elif percent_change <= -5:
    news_print()
else:
    print("Dont worry.")



