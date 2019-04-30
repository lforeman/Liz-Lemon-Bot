import tweepy as tp 
import time
import os

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_secret = os.environ.get('access_secret')

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('lemonisms')
for lemonism_image in os.listdir('.'):
    api.update_with_media(lemonism_image)
    time.sleep(3)