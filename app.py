import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the Spotify API client
scope = ["playlist-read-private", "user-library-read", "playlist-modify-public", "playlist-modify-private"]
auth_manager = SpotifyOAuth(client_id="clientID", client_secret="clientSecret", redirect_uri="http://localhost:8080", scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Set up the playlist details
playlist_id = "playlistID"
song_id = "SongID"
song_uri = f"spotify:track:{song_id}"

# Add the song to the playlist repeatedly
while True:
    sp.playlist_add_items(playlist_id, [song_uri])