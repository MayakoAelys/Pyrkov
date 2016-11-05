# -*- coding:utf-8 -*-
from markovGenerator import MarkovGenerator

# === CONFIG (x): default value
#MAXWORD = 1			# (unused)(1) Max word to take in count for the transition probability
# === /CONFIG

# Init
dummyString = "This is a dummy string. It contains some dummy values for testing purposes. It will be short, annoying, but still usefull."
markov = MarkovGenerator(dummyString)