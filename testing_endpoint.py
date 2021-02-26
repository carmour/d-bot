import requests
import json

import sample_activity

# activity_dict = sample_activity.activity_dict
activity_dict = sample_activity.activity_dict
test_dict = sample_activity.test_dict
test_dict_create = sample_activity.test_dict_create
# activity_json = json.dumps(sample_activity.activity_dict, indent=4)
# test_json = json.dumps(sample_activity.test_dict, indent=4)

# print(activity_json)
# print(test_json)

url = 'http://localhost:5000/testing'
x = requests.post(url, json = test_dict)
# x = requests.post(url, json = activity_dict)
# x = requests.post(url, json = test_dict_create)
# x = requests.post(url, data = {'some': 'data'})