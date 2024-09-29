from dotenv import load_dotenv
import os
import base64
import json
from requests import post

# Load environment variables
load_dotenv()

# Get the Spotify API credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_token():
    # Create the authorization string
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    
    # Encode the authorization string in base64 and decode it to get a string
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
    
    # Set the URL and headers for the request
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,  # Correct usage of auth_base64 as a string
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Set the data for the POST request
    data = {"grant_type": "client_credentials"}
    
    # Send the POST request to get the token
    result = post(url, headers=headers, data=data)
    
    if result.status_code == 200:
        json_result = result.json()  # Directly parse JSON response
        token = json_result["access_token"]
        return token
    else:
        raise Exception(f"Failed to retrieve token: {result.status_code}, {result.text}")

def get_auth_header():
    token = get_token()
    return {"Authorization": "Bearer " + token}

# Get and print the access token
try:
    token = get_token()
    print("Access Token:", token)
except Exception as e:
    print(e)