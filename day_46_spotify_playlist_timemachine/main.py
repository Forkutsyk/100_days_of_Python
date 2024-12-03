import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv("../.env")
BILBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")


def ask_user():
    # TODO: make a simple GUI for this , using for example Tkinter
    return input("Which year do you want to travel to ? Type the date in the format YYYY-MM-DD\n")


def data_collector(year):
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url=f'{BILBOARD_URL}{year}/', headers=header)
    response.raise_for_status()
    return response.text


def parser(data):
    soup = BeautifulSoup(data, 'html.parser')
    title_tags = soup.select('li > h3[class^="c-title"]')
    songwriter_tags = soup.select('li > span[class^="c-label"]')

    title_names = [title.getText().split("\t")[9] for title in title_tags]
    step_one = [title.getText().split("\t")[2].split("\n")[0] for title in songwriter_tags]
    step_two = [item for item in step_one if (item == '112' or not item.isdigit() and item != 'NEW' and item != '-') or ' ' in item]
    return title_names, step_two


def spotify_auth():
    auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                client_secret=SPOTIPY_CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                scope="playlist-modify-private",
                                cache_path='.cache'
                                )
    return spotipy.Spotify(auth_manager=auth_manager)


def spotify_uri_search(auth, tracks, artists):
    result = []
    for track in tracks:
        query = f"track:{track} artist:{artists[tracks.index(track)]}"
        try:
            response = auth.search(q=query, type='track')
            uri = response['tracks']['items'][0]['uri']
            result.append(uri)
        except IndexError:
            pass

    return result


def create_playlist(auth, uri_list, year):
    user_id = auth.current_user()["id"]
    song_count = len(uri_list)
    playlist_name = f"{year} Billboard {song_count}"
    output = auth.user_playlist_create(user=user_id,
                                       name=playlist_name,
                                       public=False,
                                       description=f"The {song_count} of the top 100 song from {year}")
    auth.user_playlist_add_tracks(user=user_id, playlist_id=output['id'], tracks=uri_list)
    print(f"I've created the playlist, check it out!\n{output['external_urls']['spotify']}")


if __name__ == '__main__':

    user_response = ask_user()
    clean_html = data_collector(user_response)
    titles, bands = parser(clean_html)
    sp = spotify_auth()
    list_of_song_uri = spotify_uri_search(sp, titles, bands)
    create_playlist(sp, list_of_song_uri, user_response)


