from discord_webhook import DiscordWebhook, DiscordEmbed
import os
from dotenv import load_dotenv

import helper

load_dotenv()

disco_url = os.getenv('DISCO_URL')

def push_disco(activity):
    user_id = str(activity['athlete']['id'])
    name = helper.find_user(str(activity['athlete']['id']))['name']
    activity_type = activity['name']
    activity_duration = activity['moving_time']
    activity_distance = activity['distance']/1000

    content = f"{name} just posted to Strava! This hero just went on a {activity_type} for {activity_distance}km in {activity_duration}s. What a MACHINE! Kudos!"
    
    webhook = DiscordWebhook(url=disco_url, username='Twang reloaded', content=content)
    response = webhook.execute()


# embed = DiscordEmbed(title='New Strava event!', color=242424)
# icon_url can be picture of geoff??

# webhook.add_embed(embed)