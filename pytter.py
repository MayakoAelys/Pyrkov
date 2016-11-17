# -*- coding:utf-8 -*-
import tweepy
import re
import html
from markovGenerator import MarkovGenerator

class Twitter:
    def __init__(self, consumer_key = "", consumer_secret = "", access_token = "", access_secret = ""):
        # Config
        # TODO: Make a config file
        self.pattern_username = r"(\.?@[a-zA-Z0-9_]{1,15})" # https://support.twitter.com/articles/20065832#error

        # <user>
        self.consumer_key    = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token    = access_token
        self.access_secret   = access_secret

        # Tweepy connection
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)

        # Tweets
        self.tweets = []    # Contains the last bunch of tweets retrieved with self.get_statuses()

    """
    Get the number of remaining requests before we are limited
    """
    def get_remaining_requests(self):
        return self.api.rate_limit_status()["resources"]["statuses"]["/statuses/home_timeline"]["remaining"]

    """
    Return the most recent and cleaned (see self.clean_tweet and self.is_nice_tweet) statuses from the user's timeline (up to 800)
    """
    def get_statuses(self):
        result = []
        sinceId = -1    # We can't retrieve all the statuses in one bunch
        passes = 0

        # Try to get 800 tweets (we can't get more with /statuses/home_timeline)
        # See: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
        while len(result) < 800 and self.get_remaining_requests() > 0:
            if sinceId == None:
                break

            if sinceId == -1:
                statuses = self.api.home_timeline(count=200, tweet_mode="extended")
            else:
                statuses = self.api.home_timeline(count=200, max_id=sinceId, tweet_mode="extended")

            for status in statuses:
                text = ""

                # If this is a retweet, the fetched tweet may be truncated
                try:
                    text = status.retweeted_status.full_text
                except:
                    text = status.full_text

                text = self.clean_tweet(text)
                if self.is_nice_tweet(text): result.append(text)

            backId = sinceId
            sinceId = statuses.max_id
            passes += 1

        self.tweets = result
        return result

    """
    Check if we should add the current tweet to our database
    """
    def is_nice_tweet(self, tweet):
        # We won't add tweet that only contains one link
        if tweet.startswith(("http", "https", "www")) and len(tweet.split()) == 1:
            return False

        # An empty tweet is not a nice tweet
        if tweet == "": return False

        # Validated
        return True

    def clean_tweet(self, tweet):
        # Escape HTML tags
        tweet = html.unescape(tweet)

        # Remove @ usernames (only the first one)
        while tweet.startswith(("@", ".@")):
            tweet = re.sub(self.pattern_username, "", tweet, count=1).strip()

        return tweet

if __name__ == '__main__':
    print("Please execute main.py")
    exit()