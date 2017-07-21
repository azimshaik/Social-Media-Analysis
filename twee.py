import tweepy
import keys
from tweetClass import Tweet

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

tweetObjsArray = []

#For Mentions Time Line tweets
public_tweets = api.mentions_timeline()
for tweet in public_tweets:
    #userinfo(tweet.text,tweet.user,tweet.id)
    tweeturl = 'https://twitter.com/'+tweet.user.screen_name+'/status/'+str(tweet.id)
    tweetObj = Tweet(tweet.id,tweet.user.screen_name, tweet.text, tweeturl)
    tweetObjsArray.append(tweetObj)
   
print len(tweetObjsArray)
print tweetObjsArray[0].tweet

# trends = api.trends_available()
# for trend in trends:
#     print trend.text

#For user
# user = api.get_user('iamazimadroit')
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name

# def userinfo(status,user,id):
#     print status
#     print user.screen_name
#     print 'https://twitter.com/'+user.screen_name+'/status/'+str(id)
