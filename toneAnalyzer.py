import keys
import time
import json
import emoji
import tweepy
import config
from tweetClass import Tweet
from Tone_Category_Class import Tone
from Tone_Category_Class import ToneCategory
from watson_developer_cloud import ToneAnalyzerV3

#Twetter auth
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

#watson auth
tone_analyzer = ToneAnalyzerV3(
    username=config.username,
    password=config.password,
    version='2017-06-16')

#get data from twitter - mentions timeline tweets
tweetObjsArray = []
public_tweets = api.mentions_timeline()
for tweet in public_tweets:
    #userinfo(tweet.text,tweet.user,tweet.id)
    tweeturl = 'https://twitter.com/'+tweet.user.screen_name+'/status/'+str(tweet.id)
    tweetObj = Tweet(tweet.id,tweet.user.screen_name, tweet.text, tweeturl)
    tweetObjsArray.append(tweetObj)
tweetArrayLen = len(tweetObjsArray)

#resultx =  (json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2))


def toneAnalyzHelper(result2):
    length = len(result2['document_tone']['tone_categories'][0]['tones'])
    print time.asctime( time.localtime(time.time()) )
    print '----------------------------------------------------------'
    #looping through tone_categories
    toneCatLength = len(result2['document_tone']['tone_categories'])
    i=0
    toneCategoryArray  = []
    while i<toneCatLength:
        tonesLength = len(result2['document_tone']['tone_categories'][i]['tones'])
        j=0
        category_name = result2['document_tone']['tone_categories'][i]['category_name']
        category_id = result2['document_tone']['tone_categories'][i]['category_id']
        print 'Tone Category: '+ category_name
        print '-------------------------------'
        tonesArray =  []
        while j<tonesLength:
            tone_Name =  result2['document_tone']['tone_categories'][i]['tones'][j]['tone_name']
            score = result2['document_tone']['tone_categories'][i]['tones'][j]['score']
            tone_Id = result2['document_tone']['tone_categories'][i]['tones'][j]['tone_id']
            print 'Tone Name: ' + tone_Name
            print 'Score%:  ' 
            print score*100
            tone = Tone(tone_Name, score, tone_Id)
            j+=1
            tonesArray.append(tone)
        print '----------------------------------------------------------'
        toneCategory = ToneCategory(category_id,tonesArray, category_name)
        i+=1
        toneCategoryArray.append(toneCategory)

k=0
while k < tweetArrayLen:
    result2 = tone_analyzer.tone(text=tweetObjsArray[k].tweet)
    print tweetObjsArray[k].tweet
    print "Response URL:"+ tweetObjsArray[k].url
    toneAnalyzHelper(result2)
    k+=1

print 'Unit test was successful'

    
#print toneCategoryArray[0].category_id
tonesArray = []
