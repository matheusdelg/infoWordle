from game import Game
from dataset.manipulate import WordList
from math import log2

class Word:
    def __init__ (self, word):
        self.word = word
        self.probability = {}
        self.match = {}

        wl = WordList()
        self.total = len(wl.wordlist)

        self.compareWords()

    def compareWith(self, word):
        game = Game()
        game.word = word
        result = "".join(game.guess(self.word))

        self.match[word] = result
        if result in self.probability.keys():
            self.probability[result] += 1 / self.total
        else:
            self.probability[result] = 1 / self.total

    def compareWords(self):
        wl = WordList()
        
        for guess in wl.wordlist:
            self.compareWith(guess)

class Player:
    def __init__(self):
        self.entropy = {}

    def train(self, guess):
        w = Word(guess)
        probs = w.probability

        entropies = [-probs[key]*log2(probs[key]) for key in probs.keys()]
        self.entropy[guess] = sum(entropies)

    def bestFit(self):
        return max(self.entropy, key=self.entropy.get)
    