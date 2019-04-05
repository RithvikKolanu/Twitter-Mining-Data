import tweepy
from textblob import TextBlob
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json

client = MongoClient(
    "mongodb+srv://rithvikkolanu:<password>@twitterminingdata-twph5.mongodb.net/test?retryWrites=true"
)
db = client.input
db.input.remove({})

consumer_key = "VBi8xSyHQyVTWQvsIvKhvuXs5"
consumer_secret = "klDMzRBOeDKCetaH7yWIlNRk7lN1MvZfXANXTpjvxkNHBvLMGH"
access_token = "1112897842312445952-GMVFJP6TnYxBM2PF9n2PMXXSebZ2xk"
access_secret = "JWaIfMVUzO82HzA68MhM6perPk3BmaaFS5r0tKlkLqHsP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


class MyStreamListener(StreamListener):
    def on_connect(self):
            print("you are now connected")
    def on_error(self, status_code):
            print(repr(status_code))
    def on_data(self, raw_data):

        try:
            global datajson
            datajson = json.loads(raw_data)
            db.input.insert(datajson)

            created_at = datajson['created_at']
            print(created_at)
        except Exception as e:
            print(e)




MyStreamListener = MyStreamListener()
MyStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener)

input = input("KeyWord: ")
Tracked = MyStream.filter(track=[input])



