from utils import find_none_indices

import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylistManager:
    """
    Spotify Playlist Manager
    """

    def __init__(self, client_id, client_secret, redirect_uri, cache_path):
        """
        This function initializes the SpotifyPlaylistManager class
        :param client_id:
        :param client_secret:
        :param redirect_uri:
        :param cache_path:
        """
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

    def create_playlist(self, playlist):
        """
        This function creates a playlist and adds tracks to it.
        :param playlist: An instance of the Playlist class containing playlist details.
        """
        # Create playlist and add tracks to it
        playlist.id = self.sp.user_playlist_create(user=self.user_id, name=playlist.playlist_name,
                                                   public=True, description=playlist.playlist_description)['id']
        print(f"Created playlist: {playlist.playlist_name}, {playlist.id}")

        if playlist.image_path:
            self.upload_playlist_cover_image(playlist_id=playlist.id, image_b64=playlist.image_path)

        for track in playlist.playlist_tracks:
            track_uri = self.search_track_uri(song=track['title'], artist=track['artist'])
            playlist.tracks_uris.append(track_uri)

        if None in playlist.tracks_uris:
            none_index = find_none_indices(playlist.tracks_uris)
            for index in none_index:
                print(f"Cannot add track: {playlist.playlist_tracks[index]['title']} not found with scraped data. "
                      f"Add manually at index: {index}.")

        self.add_tracks_to_playlist(playlist_id=playlist.id, track_uris=playlist.tracks_uris)

        print(f"Added tracks to playlist: {playlist.playlist_name}")

    def user_playlists(self):
        """
        This function gets the user playlists
        :return:
        """
        playlists = self.sp.user_playlists(self.user_id)
        playlist_info = {}
        # Iterate through each playlist and print its name
        for playlist in playlists['items']:
            playlist_info[playlist['name']] = {'id': playlist['id'], 'uri': playlist['uri']}
        return playlist_info

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
        This function searches for a song in Spotify with the information obtained from the Apple Music website
        :param song: Song title
        :param artist: Artist name
        :return: URI of the song if found, else None
        """
        try:
            search_query = f"track:{song} artist:{artist}"
            result = self.sp.search(search_query, type="track")

            if result["tracks"]["items"]:
                uri = result["tracks"]["items"][0]["uri"]
                print('Song found')
                return uri
        except IndexError:
            # Retry search without artist
            try:
                search_query_without_artist = f"track:{song}"
                result_without_artist = self.sp.search(search_query_without_artist, type="track")
                if result_without_artist["tracks"]["items"]:
                    for item in result_without_artist['tracks']['items'][:5]:
                        song_title = item['name']
                        artist_name = item['artists'][0]['name']
                        print(song_title, artist_name)

                index = int(input(
                    f"Which song do you want to add? from 0 to {len(result_without_artist['tracks']['items'][:5])}: if song doesn't exist, enter -1: "))
                if index == -1 or index > 4:
                    return None
                uri_without_artist = result_without_artist["tracks"]["items"][index]["uri"]
                print('Song found without artist')
                print(uri_without_artist)
                return uri_without_artist
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
                return None

        print(f"{song} doesn't exist in Spotify. Skipped.")
        return None

    def add_tracks_to_playlist(self, playlist_id, track_uris):
        """
        This function adds tracks to a playlist
        :param playlist_id:
        :param track_uris:
        :return:
        """
        if track_uris is None:
            print("Error: track_uris parameter is None")
            return

        # Filter out None values from track_uris list
        track_uris = [uri for uri in track_uris if uri is not None]

        try:
            self.sp.user_playlist_add_tracks(user=self.user_id, playlist_id=playlist_id, tracks=track_uris)
            print("Tracks added successfully")
        except Exception as e:
            print(f"Error: Failed to add tracks to playlist - {e}")

    def update_tracks_in_playlist(self, playlist):
        """
        This function updates tracks in a playlist
        :param playlist: An instance of the Playlist class
        :return: 
        """
        user_playlists = self.user_playlists()
        if playlist.playlist_name in user_playlists.keys():
            playlist.id = user_playlists[playlist.playlist_name]['id']
            for track in playlist.playlist_tracks:
                track_uri = self.search_track_uri(song=track['title'], artist=track['artist'])
                playlist.tracks_uris.append(track_uri)
            print(playlist.tracks_uris)

            # Filter out None values from track_uris list
            playlist.tracks_uris = [uri for uri in playlist.tracks_uris if uri is not None]
            print(playlist.tracks_uris)
            self.sp.user_playlist_replace_tracks(user=self.user_id, playlist_id=playlist.id, tracks=playlist.tracks_uris)
            print(f"Updated tracks in playlist: {playlist.playlist_name}")
        else:
            print(f"Playlist '{playlist.playlist_name}' not found. \n")
            print("This are the playlists you can update:\n")
            for key in user_playlists.keys():
                print(key)

    def delete_playlist(self, playlist_id):
        """
        This function deletes a playlist
        :param playlist_id:
        :return:
        """
        self.sp.user_playlist_unfollow(user=self.user_id, playlist_id=playlist_id)
        print(f"Deleted playlist with ID: {playlist_id}")
