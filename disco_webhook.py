from discord_webhook import DiscordWebhook, DiscordEmbed
import os
from dotenv import load_dotenv
import logging

import helper
import logging_handler

disco_url = os.getenv('DISCO_URL')

def push_disco(activity):
    """
    Pushes the relevant activity information to the Discord endpoint.
    """
    user_id = str(activity['athlete']['id'])
    name = helper.find_user(str(activity['athlete']['id']))['name']
    activity_type = activity['name']
    activity_duration = activity['moving_time']
    activity_distance = activity['distance']/1000

    logging_handler.posts_logger.info(f"{name} posted an activity with an ID of {activity['id']}.")
    content = f"{name} just posted to Strava! This hero just went on a {activity_type} for {activity_distance}km in {activity_duration}s. What a MACHINE! Kudos!"
    
    webhook = DiscordWebhook(url=disco_url, username='Twang reloaded', content=content)
    response = webhook.execute()