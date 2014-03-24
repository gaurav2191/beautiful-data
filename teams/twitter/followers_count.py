from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import tweepy
import time
from time import localtime, strftime, sleep
 
global api
#insert your API key
consumer_key = "dwrGczLgkm5JaT7IPI0V4A"
#insert your API secret
consumer_secret = "sqKbSuIyXvgoQPAlICKZ4ELI3GEWDeqKTtG1FuIxeZk"
#insert your access token
access_key="477508715-2po3lfEEdhiSO2iV0cGleVTlI0YcS1uYwQ88CGB2"
#insert your access token secret
access_secret="fgfcnKMcZRtKEIOFWSB53CXCZNKd5ZKOBGrfGiThHaz4H"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)
user = api.get_user('google')
a1 = user.screen_name
a2 = user.followers_count
user = api.get_user('yahoo')
b1 = user.screen_name
b2 = user.followers_count
user = api.get_user('amazon')
c1 = user.screen_name
c2 = user.followers_count
user = api.get_user('ebay')
d1 = user.screen_name
d2 = user.followers_count
saveData = a1 + "\t" + str(a2) + "\n" + b1 + "\t" + str(b2) + "\n" + c1 + "\t" + str(c2) + "\n" + d1 + "\t" + str(d2) + "\n"
saveFile = open('followers.txt','a')
saveFile.write(saveData)
saveFile.close()
