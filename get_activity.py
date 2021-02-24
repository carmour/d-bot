import requests

def get_activity(activity_id, access_token):
    return requests.get(f'https://www.strava.com/api/v3/activities/{activity_id}?access_token={access_token}').json()