from dotenv import load_dotenv
import os
from requests import post, get
import base64
import json

# Load environment variables
load_dotenv()
client_id = os.getenv("Client_id")
client_secret = os.getenv("Client_secret")

# Function to generate Spotify API token
def gen_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)

    if result.status_code != 200:
        print(f"Error: {result.status_code}, {result.text}")
        return None

    json_result = json.loads(result.content)
    return json_result.get("access_token")

# Function to get authorization header
def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

# Function to search for a song and return song details
def search_song(song_name, token):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": song_name,
        "type": "track",
        "limit": 1
    }

    response = get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    json_result = response.json()
    tracks = json_result.get("tracks", {}).get("items", [])
    
    if not tracks:
        return "No song found."

    track = tracks[0]
    song_info = {
        "name": track["name"],
        "artist": track["artists"][0]["name"],
        "album": track["album"]["name"],
        "preview_url": track.get("preview_url", "No preview available"),
        "spotify_url": track["external_urls"]["spotify"]
    }
    
    return song_info

# Example usage
token = gen_token()
if token:
    song_name = input("Enter song name: ")  # Ask user for song name
    song_info = search_song(song_name, token)
    
    if song_info:
        print("\n--- Song Details ---")
        print(f"Name: {song_info['name']}")
        print(f"Artist: {song_info['artist']}")
        print(f"Album: {song_info['album']}")
        print(f"Preview: {song_info['preview_url']}")
        print(f"Spotify Link: {song_info['spotify_url']}")
else:
    print("Failed to get token")
