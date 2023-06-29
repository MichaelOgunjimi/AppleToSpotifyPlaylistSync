from SpotifyPlaylistManager import SpotifyPlaylistManager
from playlist import Playlist

# Initialize the Playlist you want to sync to Spotify
playlist_manager = SpotifyPlaylistManager(
    client_id='your-spotify-client-id',
    client_secret='your-spotify-client-secret',
    redirect_uri="http://127.0.0.1:5500/",
    cache_path="token.txt"
)

# For multiple playlists you can use the following code:
# This will be a list dictionary with the playlist details
all_playlists = [
    {
        "playlist_url": "playlist url from Apple Music",
        "artist_name": "artist name",
        "playlist_name": "playlist name",
        "playlist_description": "playlist description"
    },
    {
        "playlist_url": "playlist url from Apple Music",
        "artist_name": "artist name",
        "playlist_name": "playlist name",
        "playlist_description": "playlist description"
    },
    {
        "playlist_url": "playlist url from Apple Music",
        "artist_name": "artist name",
        "playlist_name": "playlist name",
        "playlist_description": "playlist description"
    },
    {
        "playlist_url": "playlist url from Apple Music",
        "artist_name": "artist name",
        "playlist_name": "playlist name",
        "playlist_description": "playlist description"
    },
]

# Update playlists with the latest tracks
for playlist_info in all_playlists:
    playlist = Playlist(
        playlist_url=playlist_info['playlist_url'],
        artist_name=playlist_info['artist_name'],
        playlist_name=playlist_info['playlist_name'],
    )
    playlist_manager.update_tracks_in_playlist(playlist=playlist)
# if the playlist is does not exist it will list all the playlists available
