import requests
import os
from dotenv import load_dotenv

# Disables unverified https request warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import helper

# load_dotenv()

def find_refresh(user_id):
    """Finds a user's refresh token."""
    user = helper.find_user(user_id)
    return user['refresh_token']

def refresh_access(refresh_token, user_id):
    """Refreshes both access and refresh tokens, given a user's pre-existing refresh token."""
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
        'f': 'json'
    }
    generate_tokens = requests.post(auth_url, data=payload, verify=False)
    new_refresh_token = generate_tokens.json()['refresh_token']
    new_access_token = generate_tokens.json()['access_token']
    helper.write_tokens(new_refresh_token, new_access_token, user_id)
    return new_access_token

def return_access_token(user_id):
    """Returns new access token based on new refresh token."""
    refresh_token = find_refresh(user_id)
    access_token = refresh_access(refresh_token, user_id)
    return access_token
