import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
texts = []
links = []
for article in articles:
    text = article.get_text()
    texts.append(text)
    link = article.find("a")["href"]
    links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index = article_upvotes.index(max(article_upvotes))

print(texts[index])
print(links[index])
print(article_upvotes[index])

