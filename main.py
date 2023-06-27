from SpotifyPlaylistManager import SpotifyPlaylistManager
from playlist import Playlist
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
import os

#Instantiate playlist
liltjay_essentials = Playlist(
    playlist_url="https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
    artist_name="Lil Tjay",
    playlist_name="Lil Tjay Essentials From Apple Music",
    playlist_description= "This is Lil Tjay Essentials From Apple Music",
    image_path="https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
)

Aboogie_essentials = Playlist(
    playlist_url="https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
    artist_name="A Boogie Wit da Hoodie",
    playlist_name="A Boogie Wit da Hoodie Essentials From Apple Music",
    playlist_description= "This is A Boogie Wit da Hoodie Essentials From Apple Music",
    image_path="https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
)

buju_essentials = Playlist(
    playlist_url="https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
    artist_name="Bnxn fka Buju",
    playlist_name="Bnxn fka Buju Essentials From Apple Music",
    playlist_description= "This is Bnxn fka Buju Essentials From Apple Music",
    image_path="https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
)

Central_C_essentials = Playlist(
    playlist_url="https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
    artist_name="Central C",
    playlist_name="Central C Essentials From Apple Music",
    playlist_description= "This is Central C Essentials From Apple Music",
    image_path="https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
)

Drake_essentials = Playlist(
    playlist_url="https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
    artist_name="Drake",
    playlist_name="Drake Essentials From Apple Music",
    playlist_description= "This is Drake Essentials From Apple Music",
    image_path="https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
)


#Instantiate SpotifyPlaylistManager
playlist_manager = SpotifyPlaylistManager(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:5500/",
    cache_path="token.txt"
)
#This is your spotify user id
user_id = playlist_manager.user_id

#Add this search for the songs to identify and ready to be added
for song in liltjay_playlist.songs:
    artist = song['artist']
    title = song['title']
    liltjay_playlist.uris.append(playlist_manager.search_track_uri(title, artist))

print(liltjay_playlist.uris)

for