from flask import Flask, request, jsonify, make_response
import os
from dotenv import load_dotenv
import logging

import webhook_handler
import disco_webhook
import logging_handler
import helper

error_logger = logging_handler.setup_logger('error_logging', 'errors.log')
# error_logger.setLevel(logging.INFO)
posts_logger = logging_handler.setup_logger('post_logging', 'posts.log')
posts_logger.setLevel(logging.INFO)
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # initiates webhook -- perform CURL request to hit this endpoint
        verify_token = os.getenv('INITIATE_TOKEN')
        mode = request.args['hub.mode']
        token = request.args['hub.verify_token']
        challenge = request.args['hub.challenge']
        if (mode and token):
            if mode == 'subscribe' and token == verify_token:
                print('webhook verified!')
                response = jsonify({
                    'hub.challenge': challenge
                })
                return make_response(response), 200
            else:
                return make_response('Forbidden'), 403
    elif request.method == 'POST':
        # webhook received here
        print('request.json: ', request.json)
        new_event = request.json
        user_id = str(request.json['owner_id']) 
        activity_id = str(request.json['object_id'])
        try:
            show_biz(user_id, activity_id)
        except TypeError as e:
            print(e)
        finally:
            return make_response('Ok'), 200

    return 'x'

# TEST ROUTE -- same as webhook receipt above, tested with testing_endpoint.py module
@app.route('/testing', methods=['POST'])
def testing_route():
    if request.json['aspect_type'] == 'create':
        try:
            print('request.json: ', request.json)
            new_event = request.json
            user_id = str(request.json['owner_id'])
            # below will throw a TypeError
            # user_id = (request.json['owner_id'])
            activity_id = str(request.json['object_id'])
            show_biz(user_id, activity_id)
        except TypeError as e:
            print(e)
            error_logger.warning("TypeError: ", exc_info=True)
        except Exception as e:
            print('Unhandled error:', e)
            error_logger.warning("Unhandled error: ", exc_info=True)
        finally:
            return make_response('Ok'), 200
    else:
        print('type != create')
        user_id = str(request.json['owner_id'])
        name = private_event(user_id)['name']
        posts_logger.info(f"{name} has posted a private activity.")
        return make_response('Ok'), 200

def show_biz(user_id, activity_id):
    # print('show_biz being called')
    # test_act = webhook_handler.testing_refresh('58937648', '4820893608')
    test_act = webhook_handler.testing_refresh(user_id, activity_id)
    disco_webhook.push_disco(test_act)

def private_event(user_id):
    return helper.find_user(user_id)

if __name__ == '__main__':
    app.run()