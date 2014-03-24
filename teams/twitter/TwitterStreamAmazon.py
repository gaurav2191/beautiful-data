from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import tweepy
import time
import pydoop.hdfs as hdfs

#insert your API key
ckey = 'dwrGczLgkm5JaT7IPI0V4A'
#insert your API secret
csecret = 'sqKbSuIyXvgoQPAlICKZ4ELI3GEWDeqKTtG1FuIxeZk'
#insert your access token
atoken = '477508715-2po3lfEEdhiSO2iV0cGleVTlI0YcS1uYwQ88CGB2'
#insert your access token secret
asecret = 'fgfcnKMcZRtKEIOFWSB53CXCZNKd5ZKOBGrfGiThHaz4H'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

class listener(StreamListener):

    def on_data(self, data):
        try:
	    tweet = data.split(',"text":"')[1].split('","source')[0]
	    timestamp = data.split('{"created_at":"')[1].split('","id')[0]
	    location = data.split(',"location":"')[1].split('","url')[0]
	    time_zone = data.split(',"time_zone":"')[1].split('","geo_enabled')[0]
	    lang = data.split(',"lang":"')[1].split('","contributors_enabled')[0]
	    saveData = timestamp + "\t" + tweet + "\t" + location + "\t" + time_zone + "\t" + lang
	    #print saveData
            saveFile = open('amazonTWITDB.csv','a')
            saveFile.write(saveData)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'Failed ondata,',str(e)
            #time.sleep(5)
		
    def on_error(self, status):
        print status
		
    def on_timeout(self):
        print sys.stderr, 'Timeout...'
        return True # Don't kill the stream

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['amazon'])
