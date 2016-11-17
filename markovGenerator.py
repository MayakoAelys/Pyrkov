# -*- coding:utf-8 -*-
from random import randrange

class MarkovGenerator:
    def __init__(self, baseString = ""):
        self.dictionnary = {}
        self.firstWords = []


        if(baseString is not ""):
            self.add_sentence(baseString)


    """Add a string to the dictionnary"""
    def add_sentence(self, baseString):
        splitted = baseString.split()

        # Add the reference of the first word
        if splitted[0] not in self.firstWords:
            self.firstWords.append(splitted[0])

        # Add words to the dictionnary
        splitSize = len(splitted)
        currentWord = ""
        nextWord = ""

        for i in range(0, splitSize):
            currentWord = splitted[i]

            if i+1 >= splitSize:
                nextWord = ""
            else:
                nextWord = splitted[i+1]

            #self.add_word(currentWord, nextWord if nextWord != "" and nextWord[-1] != "." else "")
            self.add_word(currentWord, nextWord)

        # Last word of the string is followed by an EOL
        self.add_word(currentWord, "")


    """ Add "nextword" in the array of the given key. If the key doesn't already exist, it will be created. """
    def add_word(self, key, nextWord):
        try:
            self.dictionnary[key].append(nextWord)
        except:
            self.dictionnary[key] = [nextWord]

    """ Generate a sentence using a random first word from the dictionnary """
    def generate_sentence(self, maxChar = 0):
        result = ""

        # Get the first word randomly
        randomKey = self.firstWords[randrange(len(self.firstWords))]
        currentWord = randomKey
        nextWord = ""
        result += currentWord + " "

        while True:
            nextWord = self.dictionnary[currentWord][randrange(len(self.dictionnary[currentWord]))]

            if nextWord == "" or (maxChar != 0 and len(result.strip()) + len(nextWord) > maxChar):
                return result.strip()

            result += nextWord + " "
            currentWord = nextWord

    def get_indexed_key(self, index):
        i = 0

        for key in self.dictionnary.keys():
            if i == index:
                return key

            i += 1

        print("NO KEY RETURNED")


if __name__ == '__main__':
    print("Please execute main.py")
    exit()