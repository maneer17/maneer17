import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
"""export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url """
""""CLIENT_ID="899100eaaa3d423688a0262d64d2c7de"
Client_Secret="8f0f50f388174db9811064874c63aa70"""""
"""http://example.com"""
year = input("what year would you like to travel to ? YYYY-MM-DD")
url = f"https://www.billboard.com/charts/hot-100/{year}/"
respond = requests.get(url)
content = respond.text
soup = BeautifulSoup(content, "html.parser")
titles = soup.select('li h3', id="title-of-a-story")
songs = [i.text.replace("\n", '').replace("\t", '') for i in titles if titles.index(i) <= 99]
scope = "playlist-modify-private"
list_of_songs=[]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.user_playlist_create(user="0sg24wpjxg2lkq0fqo6rblhf3",name=f"{year} Billboard 100",public=False)
k=0
for i in songs:
    song=(sp.search(q=f"track: {i} year: {year[:4]}"))
    try:
        list_of_songs.append(song['tracks']['items'][0]['uri'])
    except:
        print("sorry there're some songs that don't exist in Spotify ")


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(len(list_of_songs))
sp.user_playlist_add_tracks(user="0sg24wpjxg2lkq0fqo6rblhf3",tracks=list_of_songs,playlist_id=results['id'])





