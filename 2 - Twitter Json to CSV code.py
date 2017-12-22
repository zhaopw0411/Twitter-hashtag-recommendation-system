import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


tweets_data = []
twitter = {}
for i in range(100000,1500000,100000):
    tweets_file = ""
    tweets_file = open("small_file_" + str(i) +".json", "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            if tweet['lang'] == "en":
                tweets_data.append(tweet)
        except:
            continue
    tweets_file.close()

# writing data to a dataframe from json

tweets = pd.DataFrame()
tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

 
# writing data to csv for further processing   
tweets.to_csv("tweets_final_new.csv",encoding = "utf-8")