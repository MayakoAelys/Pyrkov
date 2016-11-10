# -*- coding:utf-8 -*-
import re
import html
from twython import Twython
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

        # Twython connection
        self.twitter = Twython(self.consumer_key, self.consumer_secret, self.access_token, self.access_secret)
        try:
            self.twitter.verify_credentials()
        except:
            print("Twitter Authorization Error, please verify your keys in the config.ini file")
            exit()

        # Tweepy connection
        #self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        #self.auth.set_access_token(self.access_token, self.access_secret)
        #self.api = tweepy.API(self.auth)

    def get_statuses(self):
        result = []
        sinceId = -1    # We can't retrieve all the statuses in one bunch

        #while len(result) < 2000:
        for i in range(0, 5):
            if sinceId == None or sinceId == "":
                break

            if sinceId == -1:
                statuses = self.twitter.get_home_timeline(count=200, tweet_mode='extended')
                #statuses = self.twitter.get_home_timeline(count=200)
            else:
                #statuses = self.twitter.get_home_timeline(count=200, max_id=sinceId)
                statuses = self.twitter.get_home_timeline(count=200, max_id=sinceId, tweet_mode='extended')

            for status in statuses:
                result.append(self.clean_tweet(status["full_text"]))

                if "…" in status["full_text"]:
                    print("BORDEL")

            sinceId = statuses[len(statuses) - 1]["id"]

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