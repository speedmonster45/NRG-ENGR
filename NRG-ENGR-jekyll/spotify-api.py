from dotenv import load_dotenv
import os
import base64
import json
import requests  # Import requests module

# Load environment variables
load_dotenv()

# Get the Spotify API credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

def get_token(auth_code):
    # Create the authorization string
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    
    # Encode the authorization string in base64 and decode it to get a string
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
    
    # Set the URL and headers for the request
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Set the data for the POST request
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    # Send the POST request to get the token
    result = requests.post(url, headers=headers, data=data)
    
    if result.status_code == 200:
        json_result = result.json()  # Directly parse JSON response
        return json_result["access_token"]
    else:
        raise Exception(f"Failed to retrieve token: {result.status_code}, {result.text}")

def get_currently_playing(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to retrieve currently playing track: ' + response.text)

# Example usage
if __name__ == "__main__":
    # Assume the auth_code is captured from your callback handler after user authorization
    auth_code = input("Enter the authorization code from the callback: ")

    # Get and print the access token
    try:
        token = get_token(auth_code)
        print("Access Token:", token)

        # Get currently playing track
        currently_playing = get_currently_playing(token)
        if currently_playing and 'item' in currently_playing:
            song_name = currently_playing['item']['name']
            artist_name = currently_playing['item']['artists'][0]['name']
            progress_ms = currently_playing['progress_ms']  # Current playback position in milliseconds

            print(f"Currently Playing: {song_name} by {artist_name}")
            print(f"Current Time: {progress_ms / 1000:.2f} seconds")
        else:
            print("No track is currently playing.")
    except Exception as e:
        print(e)