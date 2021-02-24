import requests
import json
import os
from dotenv import load_dotenv

# disables unverified https request warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

# refactor
# just call ONE function in index.py
# then there is ONE function in this file that calls ALL of the required functions
# that way the only thing needed to be passed from index is user_id

# this ONE function in this file will just return the access tokens
# then, call the get_activity function using the initial user_id and the access token

def return_access_token(user_id):
    refresh_token = find_refresh(user_id)
    access_token = refresh_access(refresh_token, user_id)
    return access_token

# basically a helper function
def find_user(user_id):
    f = open('user_ids_test_2.json')
    user_data = json.load(f)
    for user in user_data:
        if user['id'] == user_id:
            return user

def find_refresh(user_id):
    user = find_user(user_id)
    # return user['refresh_token'], user_id
    return user['refresh_token']

# this is called in refresh_access func
def write_tokens(new_refresh_token, new_access_token, user_id):
    user = find_user(user_id)
    # print(user)
    with open('user_ids_test_2.json', 'r') as f:
        user_data = json.load(f)
        for item in user_data:
            if item == user:
                item['access_token'] = new_access_token
                item['refresh_token'] = new_refresh_token
    with open('user_ids_test_2.json', 'w') as f:
        json.dump(user_data, f, indent=4)

# def write_tokens(new_refresh_token, new_access_token, user_id):
#     user = find_user(user_id)
#     with open('user_ids_test.json', 'r') as f:
#         user_data = json.load(f)
#         for item in user_data:
#             if item == user:
#                 item['access_token'] = new_access_token
#                 item['refresh_token'] = new_refresh_token
#     with open('user_ids_test.json', 'w') as f:
#         json.dump(user_data, f, indent=4)

# refreshes access and refresh tokens, given user's refresh token
# def refresh_access(refresh_token, user_id):
#     client_id = os.getenv('CLIENT_ID')
#     client_secret = os.getenv('CLIENT_SECRET')
#     auth_url = "https://www.strava.com/oauth/token"
#     payload = {
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'refresh_token': refresh_token,
#         'grant_type': 'refresh_token',
#         'f': 'json'
#     }
#     generate_tokens = requests.post(auth_url, data=payload, verify=False)
#     new_refresh_token = generate_tokens.json()['refresh_token']
#     new_access_token = generate_tokens.json()['access_token']
#     write_tokens(new_refresh_token, new_access_token, user_id)
#     return new_refresh_token, new_access_token
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
    write_tokens(new_refresh_token, new_access_token, user_id)
    return new_access_token
