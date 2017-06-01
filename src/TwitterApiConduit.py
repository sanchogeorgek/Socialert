#Import the necessary methods from tweepy library
import json

import db_interface
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "74772768-I81DOutCfwOQTnv8oAqUUyLKTlmD4GR84ZAuJ4HUp"
access_token_secret = "A0xLQITnIOXyvQrnbTTBcVuccRPB8RPYvCSAcPUGWuU8b"
consumer_key = "5JsFN2Pqk19oXB1zx7qoFpADd"
consumer_secret = "eRJv4KruqbaS7od21LG9gCOaZ6PuGmqGz7ikXjtrU7tdciCK4h"

#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):

    def on_data(self, data):

        intweet = json.loads(str(data))

        tweetid = json.dumps(intweet.get('id'))
        tweethandle = json.dumps(intweet.get('user',{}).get("screen_name")).strip('"')
        tweettext = json.dumps(intweet.get('text')).strip('"').strip('''''')

        tweettext = tweettext.replace("'", "")

        # Check for presence of place-geometry in Twitter JSON Object. Only proceed if available.

        if intweet.get('place') is not None:

            tweetgeojson = json.dumps(intweet.get('place',{}).get("bounding_box"))

            db_connect = db_interface.DBInteract()

            db_connect.db_persist_tweet(tweetid,tweethandle,tweettext,tweetgeojson)

            # notresult = db_connect.db_query_email_notification()            for row in notresult:
            #
            #         emailconduit.emailwithimg("Test",row[5],row[3],row[2],row[7],row[8])
            #
            #         db_connect.db_update_post_email(row[9])

        else:

            print 'geonotavailable: ' + tweethandle + " | " + tweettext

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['bushfire','explosion','accident','flood','hurricane','fire'])