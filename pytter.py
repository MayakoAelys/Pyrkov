# -*- coding:utf-8 -*-
import tweepy
import re
import html
from markovGenerator import MarkovGenerator

class Twitter:
    def __init__(self, consumer_key = "", consumer_secret = "", access_token = "", access_secret = ""):
        # Config
        # TODO: Make a config file
        self.pattern_username = r"(@.*?\s)"

        # <user>
        self.consumer_key    = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token    = access_token
        self.access_secret   = access_secret

        # Tweepy connection
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)

    def get_statuses(self):
        result = []
        sinceId = -1    # We can't retrieve all the statuses in one bunch

        while len(result) < 2000:
            if sinceId == None:
                break

            if sinceId == -1:
                statuses = self.api.home_timeline(count=200)
            else:
                statuses = self.api.home_timeline(count=200, max_id=sinceId)

            for status in statuses:
                result.append(self.clean_tweet(status.text))

            sinceId = statuses.max_id

        return result

    def clean_tweet(self, tweet):
        # Escape HTML tags
        tweet = html.unescape(tweet)

        # Remove "RT " from retweeted tweets
        # --> We have to do this before removing @usernames otherwise it
        #     will also remove legits tweets that starts with "RT "
        tweet = tweet[3:] if tweet.startswith("RT ") else tweet

        # Remove @ usernames
        tweet = re.sub(self.pattern_username, "", tweet)

        return tweet


if __name__ == '__main__':
    # testing
    twitter = Twitter()
    markov = MarkovGenerator()
    file = open("temp.txt", "w", encoding="utf-8")

    timeline = twitter.get_statuses()
    #print(timeline)

    for status in timeline:
        markov.add_sentence(status)

    for i in range(0, 100):
        value = markov.generate_sentence(140)
        file.writelines(value + "\n")
        #print(i, ":", value)

    file.close()