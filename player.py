from game import Game
from dataset.manipulate import WordList
from math import log2

class Word:
    """ Registra informações de uma palavra: ocorrências com relação a um resultado e
        informação esperada (entropia). """

    def __repr__(self):
        return f"{self.value} - [{self.entropy}]"

    def __init__(self, word):
        self.value = word
        self.entropy = 0.
        self.occurrences = {}

    def addOccurrence(self, result, value):
        """ Registra ou incrementa o valor de ocorrência para o resultado em parâmetro."""
        if result in self.occurrences.keys():
            self.occurrences[result] += value
        else:
            self.occurrences[result]  = value

    def setEntropy(self):
        self.entropy = sum(-p * log2(p) for p in self.occurrences.values())

class Player:
    """ Calcula as entropias de um conjunto de palavras, escolhe a de maior entropia e 
        reduz o conjunto de palavras, eliminando as não correspondentes."""

    def __init__(self, wlpath=None):
        # Inicialmente, todo o conjunto de palavras deve ser considerado:
        wl = WordList(wlpath)
        self.setWordList(wl.wordlist)

    def words(self):
        """ Auxiliar para mostrar as palavras do banco. """
        return list(self.wordlist.keys())

    def setWordList(self, wordlist):
        """ Reduz o conjunto de palavras do jogador para a lista em parâmetro."""
        self.wordlist   = {word: None for word in wordlist}
        self.totalWords = len(self.wordlist)

    def calculateProbabilities(self, guess):
        """ Calcula as probabilidades do banco de palavras com relação ao 'chute'."""
        game = Game()
        game.word = guess
        for word in self.wordlist.keys():
            result = game.guess(word)
            self.addOccurrence(word, result)

    def calculateEntropies(self):
        """ Calcula as entropias (informação esperada) de cada palavra do banco. """
        for word in self.wordlist.values():
            word.setEntropy()

    def getBestFit(self):
        """ Escolhe a palavra de maior entropia do seu banco de palavras."""
        for guess in self.wordlist.keys():
                self.calculateProbabilities(guess)
        self.calculateEntropies()

        return max(self.wordlist.values(), key=lambda w: w.entropy).value

    def addOccurrence(self, word, result):
        """ Adiciona a ocorrência de um match na lista de palavras."""
        if self.wordlist[word] is None:
            self.wordlist[word] = Word(word)

        self.wordlist[word].addOccurrence(result, 1 / self.totalWords)

    def constrain(self, guess, result):
        """ Atualiza o banco de palavras com o resultado obtido em um chute. """
        words = WordList.filter(self.wordlist.keys(), guess, result)
        self.setWordList(words)

        if self.wordlist is not None:
            if guess in self.wordlist.keys():
                del self.wordlist[guess]