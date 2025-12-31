import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2025-12-12"
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id= "xxx",
        client_secret=  "xxx",
        show_dialog=True,
        cache_path="token.txt",
        username="xxx",
    )
)
user_id = sp.current_user()["id"]



filter = ["Debut Position", "Peak Position", "Chart History", "Share", "Awards", "Credits", "Songwriter(s)", "Producer(s)", "Imprint/Label", "Follow Us", "Have a Tip?", "The Daily"]
music_website = "https://www.billboard.com/charts/hot-100/"

response = requests.get(music_website)
soup = BeautifulSoup(response.content, 'html.parser')
chart_list = soup.find_all('h3', class_='c-title')
num = 1
song_names = []
for chart in chart_list[2::]:
    if num == 101:
        break
    if chart.text.strip() in filter:
        continue
    else:
        song_names.append(chart.text.strip())
        num += 1


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")