from flask import Flask, request, jsonify, make_response
import os
from dotenv import load_dotenv

import refresh_tokens
import get_activity

# app = Flask(__name__)

# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():
#     if request.method == 'GET':
#         # initiates webhook -- perform CURL request to hit this endpoint
#         verify_token = os.getenv('INITIATE_TOKEN')
#         mode = request.args['hub.mode']
#         token = request.args['hub.verify_token']
#         challenge = request.args['hub.challenge']
#         if (mode and token):
#             if mode == 'subscribe' and token == verify_token:
#                 print('webhook verified!')
#                 response = jsonify({
#                     'hub.challenge': challenge
#                 })
#                 return make_response(response), 200
#             else:
#                 return make_response('Forbidden'), 403
#     elif request.method == 'POST':
#         # webhook received here
#         print('request.json: ', request.json)
#         # print('activity id: ', request.json['object_id'])
#         new_activity = request.json
#         # give data to webhook function

#         return make_response('Ok'), 200

#     return 'hello'

# this should really be in a different file as well, maybe main.py?
def testing_refresh(user_id, activity_id):
    access_token = refresh_tokens.return_access_token(user_id)
    # print(access_token)
    print(get_activity.get_activity(activity_id, access_token))

testing_refresh('58937648', '4820893608')

# TODO: send that info to a disco webhook and DONE

# if __name__ == '__main__':
#     app.run()