#TwitterAPI Initialization Module
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob

class TwitterClient(object):
    def __init__(self):
        '''Class constructor or initialization method.'''
        # keys and tokens from the Twitter Dev Console
        consumer_key = '8hEcbFXKZwPADtWnnds5A3Xgg'
        consumer_secret = 's6L7XaN52xPBzGQHJDAYIhK8EiMirqGS4KBmNGZ3YEDqw76SZk'
        access_token = '2529158863-dfXjUwnZuCgNxZT2uyBOD3vcFqM1Dy8FbfROjZJ'
        access_token_secret = 'bbEZnGbYpcS5eLqA4jvEgLRQyPXSPReADF3MfWlV22D3r'
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed") 
    
    
