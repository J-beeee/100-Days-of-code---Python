import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.content, 'html.parser')
film_name = soup.find_all(name="h3", attrs={"class": "title"})
num = 1
with open(file="./film.txt", mode="w", encoding="utf-8") as f:
    for i in range(len(film_name))[::-1]:
        f.writelines(f'{num}) {film_name[i].text.split(" ", 1)[1]}\n')
        num += 1
