from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import base64
import requests

# Load environment variables
load_dotenv()

# Get the Spotify API credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

app = Flask(__name__)

def get_token(auth_code):
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    result = requests.post(url, headers=headers, data=data)
    if result.status_code == 200:
        return result.json()["access_token"]
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

@app.route('/now-playing', methods=['GET'])
def now_playing():
    auth_code = request.args.get('auth_code')  # Get authorization code from the query params
    try:
        token = get_token(auth_code)
        currently_playing = get_currently_playing(token)
        return jsonify(currently_playing)  # Return the data as JSON to the frontend
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)