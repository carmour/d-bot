from flask import Flask, request, jsonify, make_response
import os
from dotenv import load_dotenv
import logging

import webhook_handler
import disco_webhook
import logging_handler
import helper

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
        # strava webhook receipt handled here
        user_id = str(request.json['owner_id'])
        activity_id = str(request.json['object_id'])
        action = str(request.json['aspect_type'])
        name = helper.find_user(user_id)['name']
        print('request.json: ', request.json)
        if action == 'create':
            try:
                show_biz(user_id, activity_id)
            except TypeError as e:
                print(e)
                logging_handler.error_logger.warning("TypeError: ", exc_info=True)
            except Exception as e:
                print('Unhandled error:', e)
                logging_handler.error_logger.warning("Unhandled error: ", exc_info=True)
            finally:
                return make_response('Ok'), 200
        else:
            print('type != create')
            logging_handler.posts_logger.info(f"{name} {action}d an activity with an activity ID of {activity_id}.")
            return make_response('Ok'), 200
    return 'x'

# TEST ROUTE -- same as webhook receipt above, tested with testing_endpoint.py module
@app.route('/testing', methods=['POST'])
def testing_route():
    user_id = str(request.json['owner_id'])
    # below will throw a TypeError for testing
    # user_id = (request.json['owner_id'])
    activity_id = str(request.json['object_id'])
    action = str(request.json['aspect_type'])
    name = helper.find_user(user_id)['name']
    if action == 'create':
        try:
            print('request.json: ', request.json)
            show_biz(user_id, activity_id)
        except TypeError as e:
            print(e)
            logging_handler.error_logger.warning("TypeError: ", exc_info=True)
        except Exception as e:
            print('Unhandled error:', e)
            logging_handler.error_logger.warning("Unhandled error: ", exc_info=True)
        finally:
            return make_response('Ok'), 200
    else:
        print('request.json: ', request.json)
        print('type != create')
        logging_handler.posts_logger.info(f"{name} {action}d an activity with an activity ID of {activity_id}.")
        return make_response('Ok'), 200

def show_biz(user_id, activity_id):
    test_act = webhook_handler.testing_refresh(user_id, activity_id)
    if test_act['visibility'] == 'only_me':
        name = helper.find_user(user_id)['name']
        logging_handler.posts_logger.info(f"{name} posted a private activity with an ID of {activity_id}.")
    else:
        disco_webhook.push_disco(test_act)

if __name__ == '__main__':
    app.run()