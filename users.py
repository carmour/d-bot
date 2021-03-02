import os
from dotenv import load_dotenv

load_dotenv()

users_dict = [
    {
        "id": 12345,
        "name": "test",
        "refresh_token": os.getenv('TEST_REFRESH')
    },
    {
        "id": 58937648,
        "name": "Callum",
        "refresh_token": os.getenv('CALLUM_REFRESH')
    },
    {
        "id": 19480160,
        "name": "Patrick",
        "refresh_token": os.getenv('PATRICK_REFRESH')
    },
    {
        "id": 55218871,
        "name": "Alistair",
        "refresh_token": os.getenv('ALISTAIR_REFRESH')
    },
    {
        "id": 11034629,
        "name": "Geoff",
        "refresh_token": os.getenv('GEOFF_REFRESH')
    },
    {
        "id": 63482653,
        "name": "Gabe",
        "refresh_token": os.getenv('GABE_REFRESH')
    },
    {
        "id": 29424402,
        "name": "Henry",
        "refresh_token": os.getenv('HENRY_REFRESH')
    }
]

def find_user(user_id):
    user_dict = users_dict
    for user in user_dict:
        if user['id'] == user_id:
            return user

# user_name = find_user(12345)
# print(find_user(12345)['name'])
print(find_user(58937648)['refresh_token'])