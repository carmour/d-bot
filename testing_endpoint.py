import requests
import json

import sample_activity

# activity_dict = sample_activity.activity_dict
activity_dict = sample_activity.activity_dict
test_dict = sample_activity.test_dict
test_dict_create = sample_activity.test_dict_create
test_dict_create_private = sample_activity.test_dict_create_private
# activity_json = json.dumps(sample_activity.activity_dict, indent=4)
# test_json = json.dumps(sample_activity.test_dict, indent=4)

url = 'http://localhost:5000/testing'
# x = requests.post(url, json = test_dict)
# x = requests.post(url, json = activity_dict)
# x = requests.post(url, json = test_dict_create)
x = requests.post(url, json = test_dict_create_private)

# this one will throw an error
# x = requests.post(url, data = {'some': 'data'})