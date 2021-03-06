# EXEMPLO DE JOGO GUIADO:
from player import Player
from game import Game
from dataset.manipulate import WordList

ws = WordList("dataset/small.csv")
g = Game("dataset/small.csv")
p = Player("dataset/small.csv")

while g.loop():
    print ("Calculando entropias...")
    word = p.getBestFit()

    print (f"Melhor palavra: {word}\n")

    word = g.input()
    result = g.guess(word)

    print ("Reduzindo resultados...")
    p.constrain(word, result)

    print (p.words())
    print (g)

print (f"Palavra: {g.word}\n")