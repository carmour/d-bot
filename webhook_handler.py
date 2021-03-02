import refresh_tokens
import get_activity

def testing_refresh(user_id, activity_id):
    """ Returns access token and activity id to be used in GET request to Strava API. """
    access_token = refresh_tokens.return_access_token(user_id)
    return get_activity.get_activity(activity_id, access_token)