from dataset.manipulate import WordList
import re

class Game:

    def __init__(self, maxRounds=6):
        self.wl = WordList()
        self.maxRounds = maxRounds
        self.newTurn()

    def newTurn(self):
        self.word = self.wl.getRandom()
        self.round = 1
        self.guesses = []

    def __str__(self):
        fmtd = ["".join(guess) for guess in self.guesses]
        return "\n".join(fmtd)

    def guess(self, word):
    # TODO: "oeste" gera 1 "Y" extra em "marte" com a letra "E".
        self.round += 1
        result = ["B"] * 5

        for i, letter in enumerate(word):
            if letter in self.word:
                result[i] = "Y"
            if letter == self.word[i]:
                result[i] = "G"

        self.guesses.append(result)
        return result

    def input(self):

        valid  = False
        iregex = re.compile("^[A-Z,a-z]{5}$")

        while not valid:
            guess = input(f"Palavra da rodada {self.round}: ")
            guess = self.wl.normalize(guess)
            guess = guess.upper()

            if iregex.match(guess) and guess in self.wl.wordlist:
                valid = True
                return guess
            else:
                print ("Entrada inválida. Confira o número de caracteres e se a palavra existe.")

    def loop(self):
        conditions = ['G'] * 5 in self.guesses
        conditions = conditions or (self.round > self.maxRounds)
        return not conditions
