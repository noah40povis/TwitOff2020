from __future__ import unicode_literals
import tweepy
import os
from dotenv import load_dotenv
from tweepy import OAuthHandler, API 


load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
# print("API AUTH:", auth)

api = API(auth)
print("API CLIENT:", api)
# def twitter_api():
#     auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
#     auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
#     print("AUTH", auth)
#     api = tweepy.API(auth)
#     print("API", api)
#     #print(dir(api))
#     return api


if __name__ == "__main__":

    user = api.get_user("NewsfeedNoah")
    #user = api.user_timeline("NewsfeedNoah", tweet_mode="extended", count=150, exclude_replies=False, include_rts=False)
    print("TWITTER USER:", type(user))
    print(user.id)
    print(user.screen_name)
    print(user.name)

    tweets = api.user_timeline("NewsfeedNoah", tweet_mode="extended")
    print("TWEETS", type(tweets))
    print(type(tweets[0]))

    tweet = tweets[0]
    print(tweet.id)
    print(tweet.full_text)


#working on these print statement errors wondering why resultset has no attribute screen_name
#keep trying to debuh also remember -> might be error from __future__ import unicode_literals


