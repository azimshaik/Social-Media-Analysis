import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

def userinfo(status,user,id):
    print status
    print user.screen_name
    print 'https://twitter.com/'+user.screen_name+'/status/'+str(id)
    

#For Mentions Time Line tweets
public_tweets = api.mentions_timeline()
for tweet in public_tweets:
    #print tweet.text
    #print tweet.id
    #print tweet.geo
    #print tweet.lang
    #print tweet.retweet_count
    userinfo(tweet.text,tweet.user,tweet.id)

    #print tweet.place
    

# trends = api.trends_available()
# for trend in trends:
#     print trend.text

#For user
# user = api.get_user('iamazimadroit')
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name
