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
# You initialize the Playlist a new playlist details you to update make sure same name is used before
# Include the paramaters of what you want to update in the playlist d
Playlist = Playlist(
    playlist_url="playlist url from Apple Music",
    artist_name="artist name",
    playlist_name="playlist name",
)

playlist_manager.update_tracks_in_playlist(playlist=Playlist)


# if the playlist is does not exist it will list all the playlists available
