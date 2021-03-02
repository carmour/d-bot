<h1>D-Bot</h1>

Python Flask app that automatically posts users' Strava events to Discord server, thereby notifying all Discord users when a user posts an activity to Strava.

<h2>Overview</h2>

Multi-functional Discord bot running on a Flask server that automatically pushes users' Strava events to Discord. Application receives Strava generated webhook and uses this data to make a GET request to the Strava API to retrieve data regarding newly posted event. This information is then pushed to a Discord server via webhook. Authentication and authorization access to Strava app are controlled by OAuth. Currently running app via a Flask server sitting behind Nginx hosted on a publicly accessible Raspberry Pi on my local network. This was achieved by generating and maintaing a static IP address for the Pi, and permitting limited external contact through port forwarding.

<h2>Technologies</h2>
<ul>
<li>HTTP requests conducted by Python requests library</li>
<li>Automatically generated OAuth 2.0 user access tokens handled in app to ensure privacy of user data</li>
<li>Automated error and successful post logging facilitated by Python logging library</li>
<li>Flask server running behind Nginx hosted on Raspberry Pi</li>
<li>Networking and public access of local device managed by generating static IP address and port forwarding</li>
</ul>

I undertook this project in this manner to not only develop my Python programming skills, but also to practice web hosting, server management, and networking by hosting the application on a physical device within my network.

<h2>Further Action</h2>

This is an ongoing project. I have plans to implement:
- Simple user/bot interaction, enabling users to request 
- Database for storing activity data to compile leaderboards, store data for future reference
