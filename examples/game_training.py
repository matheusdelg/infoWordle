# EXEMPLO DE TREINAMENTO DO JOGADOR:
from player import Player
from game import Game
from dataset.manipulate import WordList

ws = WordList("dataset/small.csv")
g = Game("dataset/small.csv")
p = Player("dataset/small.csv")

best = p.getBestFit()
print (f"Melhor fit: {best}. Entropia: {p.wordlist[best].entropy}")