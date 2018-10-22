import tweepy
from textblob import TextBlob

consumer_key = 'oMh9JU4ud2qHsKTXEwJgmU7OH'
consumer_secret = 'UQ8sjskjFQnBovaZKbTyWxyJvUrd1KeTQ3tlCCElHG0l3q2luT'

access_token = '1054112079525769217-MMZ3nlujZDPNMUmIsdzb2nGjvsvg9d'
access_token_secret = 'UVcVRPueg4elSlTPy8duKgMFeOkH1odjqPzWFoAoRZTga'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
