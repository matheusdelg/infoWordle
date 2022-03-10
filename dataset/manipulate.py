import csv, unicodedata, re, random
#from player import Word 

class WordList:
    def __init__(self, path=None, delim=",", enc="utf-8"):
        self.wordlist = self.load(path, delim, enc)

    def load(self, path=None, delim=",", enc="utf-8"):
        if path is None:
            path = "dataset/words.csv"

        with open(path, encoding=enc) as f:
            reader = csv.reader(f, delimiter=delim)
            wordlist  = [self.normalize(word[0]) for word in reader]

            return wordlist

    def normalize(self, word):
        word = unicodedata.normalize("NFD", word).encode('ASCII', 'ignore').decode('utf-8')
        return str.upper(word)

    def __str__(self):
        return str(self.wordlist)

    def getRandom(self):
        return random.choice(self.wordlist)

    def filter(words, guess, result):
        regex = WordList.setRegex(guess, result)
        return list(filter(regex.match, words))
    
    def setRegex(guess, result):
        regex = "^"; ahead = ""
        for k, match in enumerate(result):
            if match == "G":
                regex += guess[k]
            elif match == "Y":
                regex += "."
                ahead += f"(?=.*[{guess[k]}].*)"
            else:
                ahead += f"(?=.*[^{guess[k]}].*)"
                regex += "."
        regex += "$"
        return re.compile(ahead + regex)

