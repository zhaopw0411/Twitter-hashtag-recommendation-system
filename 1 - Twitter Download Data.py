
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='' 
csecret=''
atoken=''
asecret=''

class listener(StreamListener):
    def on_data(self,data):
       try:
            print data
            savefile=open('twitter_data.txt','a')
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
       except BaseException,e:
            print 'failed on data',str(e)
            time.sleep(5)   

    def on_error(self,status):
        print status

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["trump"])