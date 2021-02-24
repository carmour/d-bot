from discord_webhook import DiscordWebhook, DiscordEmbed

# from helper import find_user

# message to be posted
content = f"this is the message that will be posted"

webhook = DiscordWebhook(url='', username='Twang reloaded', content=content)

embed = DiscordEmbed(title='New Strava event!', color=242424)
# can have a url set here that 
# icon_url can be picture of geoff?
embed.set_author(name='Twang bot! Yeah!', url='', icon_url='')

webhook.add_embed(embed)
response = webhook.execute()