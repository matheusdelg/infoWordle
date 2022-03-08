from game import Game
from dataset.manipulate import WordList
from math import log2

class Word:
    def __init__ (self, word):
        self.word = word
        self.probability = {}
        self.match = {}
        self.compareWords()

    def compareWith(self, word):
        game = Game()
        game.word = word
        result = "".join(game.guess(self.word))

        self.match[word] = result
        if result in self.probability.keys():
            self.probability[result] += 1.
        else:
            self.probability[result] = 1.

    def compareWords(self):
        wl = WordList()
        total = len(wl.wordlist)

        for guess in wl.wordlist:
            self.compareWith(guess)

        for result in self.probability.keys():
            self.probability[result] /= total

class Player:
    def __init__(self):
        self.entropy = {}

    def train(self, guess):
        w = Word(guess)
        probs = w.probability
        infos = {key: -log2(value) for (key, value) in probs.items()}

        entropies = [probs[key]*infos[key] for key in probs.keys()]
        self.entropy[guess] = sum(entropies)
        return self.entropy

    def bestFit(self):
        return max(self.entropy, key=self.entropy.get)
    