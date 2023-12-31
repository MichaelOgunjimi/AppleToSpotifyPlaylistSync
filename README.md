# AppleToSpotifyPlaylistSync

# Spotify Playlist Manager

This is a Python script that manages Spotify playlists by creating new playlists and updating existing ones. It utilizes
the Spotify Web API, Spotipy library, and web scraping to retrieve playlist details from Apple Music.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required Python packages installed (see `requirements.txt`)
- Spotify API credentials (client ID and client secret)
    Check the Spotipy's full documentation is online at [Spotipy Documentation](http://spotipy.readthedocs.org/) <br> or the [Spotipy GitHub Repo](https://github.com/spotipy-dev/spotipy) the [tutorial.md](https://github.com/spotipy-dev/spotipy/blob/master/TUTORIAL.md) to get started.
- Environment variables set in a `.env` file (see `.env.example` for required variables)

## Installation

1. Clone this repository:
```bash
    git clone https://github.com/MichaelOgunjimi/AppleToSpotifyPlaylistSync.git
```
```bash
    cd spotify-playlist-manager
```

2. Install the required packages using pip:
```bash
    pip install -r requirements.txt    
```


3. Set up your environment variables by creating a `.env` file based on the [`.env.example`](.env.example) file or edit the below with your credentials and run.
```bash
    ni ".env"
    echo "CLIENT_ID=YOUR-SPOTIFY-CLIENT-ID" >> .env
    echo "CLIENT_SECRET=YOUR-SPOTIFY-CLIENT-SECRET" >> .env

```

## Usage

1. Open the `main.py` file and modify the `playlist_manager` and the `playlist`to include your desired playlists. Each playlist
   should have the following properties:

   - `playlist_url`: The URL of the playlist on Apple Music.
   - `artist_name`: The name of the artist associated with the playlist.
   - `playlist_name`: The desired name for the playlist on Spotify.
   - `playlist_description`: The desired description for the playlist on Spotify.
   - `image_path`: The URL or local path of the playlist cover image .
     - You can exclude this if you do not want to add image to your playlist.


   - In the `main.py` you can uncomment the last if statement or modify if you want to automate the program to update on a particular day:<br>
     * Preview of the statement look like this:
      ```python
           if get_current_day_of_week() == "Monday":
           for playlist in essential_playlist:
           playlist_manager.update_tracks_in_playlist(playlist=playlist)
       ```


2. Run the script:
   ```bash
      python main.py
   ```

The script will perform the following actions:

- Instantiate the `SpotifyPlaylistManager` class and authenticate with the Spotify API.
- Create Spotify playlists based on the `New_Playlist` make sure you have modified this to with the correct variables
  -  See the [example](example) folder for the exampele of the action you want to run
- Add tracks to the created playlists by searching for them on Spotify using the Apple Music playlist details.
- Update the existing playlists on Mondays by replacing the tracks with the latest ones from Apple Music.

## Customization

- If you want to customize the behavior of the script, you can modify the following files:
- `SpotifyPlaylistManager.py`: Contains the `SpotifyPlaylistManager` class, which handles interactions with the Spotify
  API.
- `Playlist.py`: Contains the `Playlist` class, which represents a playlist and handles web scraping of Apple Music
  playlist details.
- `utils.py`: Contains utility functions used by the main script.

Feel free to explore and customize the code according to your needs!

## Contribution

Contributions are welcome! Here are a few guidelines to get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your modifications and ensure they adhere to the coding style.
4. Write tests to validate your changes (if applicable).
5. Commit your changes and push them to your fork.
6. Submit a pull request detailing your changes and their benefits.

Please ensure that you follow the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to this project.

## License

This project is licensed under the [MIT License](LICENSE.md)