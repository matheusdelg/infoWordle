import csv, unicodedata, re, random

class WordList:

    def __init__(self, path="dataset/words.csv", delim=",", enc="utf-8"):
        self.wordlist = self.load(path, delim, enc)

    def load(self, path, delim=",", enc="utf-8"):
        with open(path, encoding=enc) as f:
            reader = csv.reader(f, delimiter=delim)
            wordlist = [self.normalize(word[0]) for word in reader]

            return wordlist

    def normalize(self, word):
        word = unicodedata.normalize("NFD", word).encode('ASCII', 'ignore').decode('utf-8')
        return str.upper(word)

    def __str__(self):
        return str(self.wordlist)

    def getRandom(self):
        return random.choice(self.wordlist)