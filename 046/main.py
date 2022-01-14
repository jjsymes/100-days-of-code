import datetime as dt
import requests
from calendar import monthrange
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI= os.environ['SPOTIPY_REDIRECT_URI']


def number_of_days_in_month(year, month):
    return monthrange(year, month)[1]


def validate_date(string):
    current_time = dt.datetime.now()
    valid = True
    date_segments = string.split("-")
    if len(date_segments) != 3:
        valid = False
    elif len(date_segments[0]) != 4 or len(date_segments[1]) != 2 or len(date_segments[2]) != 2:
        valid = False
    elif not date_segments[0].isdigit() or not date_segments[1].isdigit() or not date_segments[0].isdigit():
        valid = False
    elif int(date_segments[1]) > 12 or int(date_segments[2]) > number_of_days_in_month(int(date_segments[1]), int(date_segments[1])):
        valid = False
    elif int(date_segments[0]) > current_time.year or int(date_segments[0]) < 1958:
        valid = False
    elif int(date_segments[0]) == current_time.year:
        if int(date_segments[1]) == current_time.month:
            if int(date_segments[2]) > current_time.day:
                valid = False
    elif int(date_segments[0]) == 1958:
        if int(date_segments[1]) == 8:
            if int(date_segments[2]) < 4:
                valid = False

    return valid

def get_date():
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    if not validate_date(date):
        print("Invalid date.")
        date = get_date()
    return date

date = get_date()

BASE_URL = "https://www.billboard.com/charts/hot-100"

url = f"{BASE_URL}/{date}"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
chart_item_html_elements = soup.find_all(name="div", class_="o-chart-results-list-row-container")
top_100_songs = []
for chart_item in chart_item_html_elements:
    top_100_songs.append(
        {
            "title": chart_item.find(name="h3", class_="c-title").get_text().strip("\n"),
            "artist": chart_item.find_all(name="span", class_="c-label")[1].get_text().strip("\n"),
        }
    )


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

current_user = sp.current_user()["id"]

track_ids = []

for track in top_100_songs:
    search_result = sp.search(q=f"{track['title']} {track['artist']}", limit=1, type="track")
    try:
        track_ids.append(search_result["tracks"]["items"][0]["id"])
    except IndexError:
        pass

playlist = sp.user_playlist_create(current_user, f"Billboard Top 100 {date}", public=False)
sp.playlist_add_items(playlist["id"], track_ids)
