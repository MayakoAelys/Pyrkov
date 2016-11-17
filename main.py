# -*- coding:utf-8 -*-
import configparser
import os
from pytter import Twitter
from markovGenerator import MarkovGenerator

CONFIG_FILE = "config.ini"

if __name__ == '__main__':
    scriptdir =  os.path.dirname(os.path.abspath(__file__))
    os.chdir(scriptdir)

    config = configparser.ConfigParser()

    if not config.read(CONFIG_FILE):
        config["auth"] = {
            "consumer_key": "YOUR CONSUMER KEY",
            "consumer_secret": "YOUR CONSUMER SECRET KEY",
            "access_token": "YOUR ACCESS TOKEN",
            "access_secret": "YOUR ACCESS SECRET KEY"
        }

        config["preferences"] = {
            "local": True
        }

        with open(CONFIG_FILE, "w") as configFile:
            config.write(configFile)

        print("Config file (config.ini) was not found and has been recreated, please configure your keys.")
        print("If it doesn't already done, create an app on https://apps.twitter.com")
        exit()

    twitter = Twitter(config["auth"]["consumer_key"], config["auth"]["consumer_secret"], config["auth"]["access_token"], config["auth"]["access_secret"])

    if twitter.get_remaining_requests() > 0:
        markov = MarkovGenerator()
        timeline = twitter.get_statuses()

        for status in timeline:
                markov.add_sentence(status)

        # Post tweet or just write generated sentences in a file?
        if config["preferences"]["local"].lower() == "false":
            twitter.post_tweet(markov.generate_sentence(140))
            print("Tweet posted!")
        else:
            # [DEBUG PURPOSE] Write original tweets in a file
            file = open("temp_tweets.txt", "w", encoding="utf-8")

            for tweet in twitter.tweets:
                file.writelines("\n[" + tweet + "]\n")

            file.close()

            # Write generated sentences in a file
            file = open("temp.txt", "w", encoding="utf-8")

            for i in range(0, 200):
                value = markov.generate_sentence(140)
                file.writelines(value + "\n")

            file.close()
            print("Tweets generated in temp.txt file")

    else:
        print("API Rate Exceeded")