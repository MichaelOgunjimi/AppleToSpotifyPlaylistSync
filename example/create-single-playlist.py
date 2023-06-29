from SpotifyPlaylistManager import SpotifyPlaylistManager
from playlist import Playlist

# Initialize the Playlist you want to sync to Spotify
playlist_manager = SpotifyPlaylistManager(
    client_id='your-spotify-client-id',
    client_secret='your-spotify-client-secret',
    redirect_uri="http://127.0.0.1:5500/",
    cache_path="token.txt"
)

# For a single playlist you can use the following code:
Playlist = Playlist(
    playlist_url="playlist url from Apple Music",
    artist_name="artist name",
    playlist_name="playlist name",
    playlist_description="playlist description",
)
playlist_manager.create_playlist(playlist=Playlist)


