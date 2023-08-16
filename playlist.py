import requests
from bs4 import BeautifulSoup
import base64
from PIL import Image
from io import BytesIO
from pprint import pprint
import json


def convert_image_to_base64(image_path: str) -> str:
    """
    This function converts an image to base64 it allows jpeg, png, gif, webp
    :param image_path:
    :return base64_data:
    """
    response = requests.get(image_path)
    image_content = response.content
    image = Image.open(BytesIO(image_content))

    # Convert the image to RGB if it has an alpha channel (e.g., PNG)
    if image.mode != "RGB":
        image = image.convert("RGB")

    with BytesIO() as buffer:
        image.save(buffer, format="JPEG" if image.format == "JPEG" else "PNG")
        base64_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return base64_data


class Playlist:
    """
    Playlist
    """

    def __init__(self, playlist_url: str, playlist_name: str, artist_name: str = None, image_path=None,
                 playlist_id=None, playlist_description=None):
        self.tracks_uris = []
        self.url = playlist_url
        self.playlist_name = playlist_name
        self.artist_name = artist_name
        self.image_path = convert_image_to_base64(image_path)
        self.result = self.get_playlist_details()
        self.playlist_description = playlist_description if playlist_description else f"This is {self.artist_name} playlist from Apple Music"
        self.playlist_tracks = self.result
        self.id = playlist_id

    def get_playlist_details(self):
        """
        This function gets the details of the playlist by scraping the Apple Music Website
        :return songs_details a list of dictionaries:
        """
        songs_details = []
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract song titles and artists
            song_titles = soup.select('.songs-list-row__song-name')
            artists = soup.select('.songs-list__song-link-wrapper a')

            for title, artist in zip(song_titles, artists):
                song_title = title.text.replace("*", "i").replace("[", "").replace("]", "")
                artist_name = artist.text
                songs_details.append({"title": song_title, "artist": artist_name})

            if not songs_details:
                playlists_details = soup.find('script', type='application/json')
                if playlists_details:
                    json_data = playlists_details.string.strip()
                    data_dict = json.loads(json_data)
                    if data_dict:
                        response = data_dict[0]["data"]["sections"][1]["items"]
                        for playlist in response:
                            songs_details.append(
                                {'title': playlist["title"], 'artist': playlist["artistName"]})
                else:
                    raise ValueError("No JSON data found in the HTML response.")

        except requests.RequestException as e:
            raise ValueError(f"An error occurred while fetching the URL: {e}")

        except (ValueError, json.JSONDecodeError) as e:
            raise ValueError(f"An error occurred while parsing the JSON data: {e}")

        for track in songs_details:
            print(f'Song title: {track["title"]} \t\tSong by: {track["artist"]}')
        return songs_details
