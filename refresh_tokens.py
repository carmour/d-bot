import requests
# import json
import os
from dotenv import load_dotenv

# disables unverified https request warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import helper

load_dotenv()

def return_access_token(user_id):
    refresh_token = find_refresh(user_id)
    access_token = refresh_access(refresh_token, user_id)
    return access_token

def find_refresh(user_id):
    user = helper.find_user(user_id)
    return user['refresh_token']

# refreshes access and refresh tokens, given user's refresh token
def refresh_access(refresh_token, user_id):
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
    # can we just not write to file? remove storage of access tokens -- for heroku hosting
    helper.write_tokens(new_refresh_token, new_access_token, user_id)
    return new_access_token
