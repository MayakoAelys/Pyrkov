# -*- coding:utf-8 -*-
from random import randrange

class MarkovGenerator:
    def __init__(self, baseString = ""):
        self.dictionary = {}
        self.firstWords = []
        self.lastWords = []


        if(baseString is not ""):
            self.add_sentence(baseString)


    """Add a string to the dictionary"""
    def add_sentence(self, baseString):
        splitted = baseString.split()

        # Add the reference of the first word
        if splitted[0].lower() not in (word.lower() for word in self.firstWords):
            self.firstWords.append(splitted[0])

        # Add the reference of the last word
        if splitted[len(splitted) - 1].lower() not in (word.lower() for word in self.lastWords):
            self.lastWords.append(splitted[len(splitted) - 1])

        # Add words to the dictionary
        splitSize = len(splitted)
        currentWord = ""
        nextWord = ""

        for i in range(0, splitSize):
            currentWord = splitted[i]

            if i+1 >= splitSize:
                nextWord = ""
            else:
                nextWord = splitted[i+1]

            self.add_word(currentWord, nextWord)

        # Last word of the string is followed by an EOL
        self.add_word(currentWord, "")


    """ Add "nextword" in the array of the given key. If the key doesn't already exist, it will be created. """
    def add_word(self, key, nextWord):
        try:
            self.dictionary[key].append(nextWord)
        except:
            self.dictionary[key] = [nextWord]

    """ Generate a sentence using a random first word from the dictionary """
    def generate_sentence(self, maxChar = 0, forceLastWord = True):
        result = ""

        while True:
            # Get the first word randomly
            randomKey = self.firstWords[randrange(len(self.firstWords))]
            currentWord = randomKey
            nextWord = ""
            result += currentWord + " "

            while True:
                nextWord = self.dictionary[currentWord][randrange(len(self.dictionary[currentWord]))]

                if nextWord == "" or (maxChar != 0 and len(result.strip()) + len(nextWord) > maxChar):
                    # Check if the last word is in the dictionary of the last word
                    tmp = result.split()

                    # if forceLastWord == true: Loop until the last word of the generated sentence is
                    #    in the dictionary of the last words (self.lastWords)
                    if forceLastWord and tmp[len(tmp)-1].lower() in (word.lower() for word in self.lastWords):
                        return result.strip()

                    # else: retry to do an other sentence

                result += nextWord + " "
                currentWord = nextWord


    def get_indexed_key(self, index):
        i = 0

        for key in self.dictionary.keys():
            if i == index:
                return key

            i += 1

        print("NO KEY RETURNED")


if __name__ == '__main__':
    print("Please execute main.py")
    exit()