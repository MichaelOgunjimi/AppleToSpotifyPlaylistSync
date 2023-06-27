import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylistManager:
    """
    Spotify Playlist Manager
    """
    def __init__(self, client_id, client_secret, redirect_uri, cache_path):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope='playlist-modify-public playlist-modify-private ugc-image-upload',
                redirect_uri=redirect_uri,
                client_id=client_id,
                client_secret=client_secret,
                show_dialog=True,
                cache_path=cache_path
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self, name, description, public=True):
        """
        This function creates a playlist and returns the playlist id
        :param name:
        :param description:
        :param public:
        :return playlist_id:
        """
        playlist = self.sp.user_playlist_create(user=self.user_id, name=name, public=public, description=description)
        return playlist['id']

    def upload_playlist_cover_image(self, playlist_id, image_b64):
        """
        This function uploads the playlist cover image
        :param playlist_id:
        :param image_b64:
        :return None:
        """
        self.sp.playlist_upload_cover_image(playlist_id=playlist_id, image_b64=image_b64)

    def search_track_uri(self, song, artist):
        """
        This function searches for a song in Spotify with the information gotten from Apple Music Website
        :param song:
        :param artist:
        :return uri of the song:
        """
        result = self.sp.search(f"track:{song} artist:{artist}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            print('Song found')
            return uri
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
            return None

    def add_tracks_to_playlist(self, playlist_id, track_uris):
        """
        This function adds tracks to a playlist
        :param playlist_id:
        :param track_uris:
        :return:
        """
        self.sp.user_playlist_add_tracks(user=self.user_id, playlist_id=playlist_id, tracks=track_uris)

    def update_tracks_in_playlist(self, playlist_id, track_uris):
        """
        This function updates tracks in a playlist
        :param playlist_id: 
        :param track_uris: 
        :return: 
        """
        self.sp.user_playlist_replace_tracks(user=self.user_id, playlist_id=playlist_id, tracks=track_uris)
