import oauth2 as oauth
import json
from urllib.parse import quote
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, USER


class Twitter:

    def __init__(self):

        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)

        self.client = oauth.Client(consumer, access_token)

    def __post(self, url):

        response, data = self.client.request(url, "POST")

    def __get(self, url):

        response, data = self.client.request(url, "GET")

        return data

    def postTweet(self, message):

        message = quote(message, safe='')
        url = "https://api.twitter.com/1.1/statuses/update.json?status="+message

        self.__post(url)

        return

    def getFeed(self):

        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + USER

        data = self.__get(url)

        tweets = json.loads(data.decode('utf-8'))

        return tweets
