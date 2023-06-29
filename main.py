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