import oauth2 as oauth
import json
from urllib.parse import quote

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

ACCESS_KEY = ""
ACCESS_SECRET = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/update.json?status="+quote('Ik test nog een keer #testen', safe='')
response, data = client.request(timeline_endpoint,"POST")


print(data)
print(response)
#tweets = json.loads(data)
#for tweet in tweets:
#    print (tweet['text'])