import requests

def get_activity(activity_id, access_token):
    """Performs GET request to Strava API to retrieve data on posted activity."""
    return requests.get(f'https://www.strava.com/api/v3/activities/{activity_id}?access_token={access_token}').json()
