import json

def find_user(user_id):
    """Finds user in user_ids.json file based on user ID."""
    f = open('user_ids.json')
    user_data = json.load(f)
    for user in user_data:
        if user['id'] == user_id:
            return user

def write_tokens(new_refresh_token, new_access_token, user_id):
    """Writes new refresh and access token to user_ids.json file."""
    user = find_user(user_id)
    with open('user_ids.json', 'r') as f:
        user_data = json.load(f)
        for item in user_data:
            if item == user:
                item['access_token'] = new_access_token
                item['refresh_token'] = new_refresh_token
    with open('user_ids.json', 'w') as f:
        json.dump(user_data, f, indent=4)