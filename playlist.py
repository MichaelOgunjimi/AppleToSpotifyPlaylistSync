import requests
from bs4 import BeautifulSoup
import base64
from PIL import Image
from io import BytesIO


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

    def __init__(self, playlist_url: str, playlist_name: str, artist_name: str, image_path=None, playlist_id=None, playlist_description=None):
        self.url = playlist_url
        self.playlist_name = playlist_name
        self.artist_name = artist_name
        self.image_path = convert_image_to_base64(image_path)
        self.result = self.get_playlist_details()
        self.description = playlist_description if playlist_description else f"This is {self.artist_name} playlist from Apple Music"
        self.songs = self.result[0]
        self.id = playlist_id
        self.uris = []

    def get_playlist_details(self):
        """
        This function gets the details of the playlist by scraping the Apple Music Website
        :return songs_details a list of dictionaries:
        """
        songs_details = []
        song_artists = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        artists = soup.find_all('div', class_='songs-list__song-link-wrapper')
        song_titles = soup.find_all(name="div", class_="songs-list-row__song-name svelte-17mxcgw")
        song_titles = [song_title.text for song_title in song_titles]
        for i in range(0, len(artists), 2):
            artist = artists[i].find_all('a')
            artist = ', '.join(a.text for a in artist)
            song_artists.append(artist)

        # This loops through both songs and artists to create a list of dictionaries
        for song_title, artist in zip(song_titles, song_artists):
            songs_details.append({"title": song_title, "artist": artist})
        return [songs_details]
