import refresh_tokens
import get_activity

def testing_refresh(user_id, activity_id):
    access_token = refresh_tokens.return_access_token(user_id)
    # print(access_token)
    return get_activity.get_activity(activity_id, access_token)