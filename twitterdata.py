from twython import Twython

twitter = Twython('API key', 'consumer key')

for status in twitter.search(q='"keybank"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print
    

