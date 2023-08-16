from SpotifyPlaylistManager import SpotifyPlaylistManager
from playlist import Playlist
from dotenv import load_dotenv
from utils import *

# Load variables from .env file
load_dotenv()
import os

# Instantiate SpotifyPlaylistManager
playlist_manager = SpotifyPlaylistManager(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:5500/",
    cache_path="token.txt"
)

# Initialize the Playlist you want to sync to Spotify
New_Playlist = Playlist(
    playlist_url="playlist url from Apple Music",
    artist_name="artist name",
    playlist_name="playlist name",
    playlist_description="playlist description",
    image_path="image path"
)

# # This will be useful if use have multiple playlists and want them to be updated on a daily or weekly basis
# if get_current_day_of_week() == "Monday":
#     playlist_manager.update_tracks_in_playlist(playlist=New_Playlist)


essential_playlists = [
    {
        "playlist_url": "https://music.apple.com/gb/playlist/lil-tjay-essentials/pl.d64fb38267b446edba8f6fa7035df0e9",
        "artist_name": "Lil Tjay",
        "playlist_name": "Lil Tjay Essentials From Apple Music",
        "playlist_description": "This is Lil Tjay Essentials From Apple Music update every Monday",
        "image_path": "https://is2-ssl.mzstatic.com/image/thumb/Features115/v4/45/b2/a4/45b2a4c9-237f-bd45-fa2b-857efc0fdbd6/pr_source.png/305x305SC.FPESS03.webp?l=en-GB"
    }
]
