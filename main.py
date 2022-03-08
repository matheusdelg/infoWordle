'''
# EXEMPLO DE JOGO:
from game import Game

game = Game()

while game.loop():
    word = game.input()
    game.guess(word)

    print (game)

print (f"Palavra: {game.word}\n")
'''

# EXEMPLO DE TREINAMENTO DO JOGADOR:
from player import Player
from game import Game
from dataset.manipulate import WordList

p = Player()
wl = WordList()
g = Game()

for word in wl.wordlist:
    print (f"Treinando jogador com {word}...")
    p.train(word)
print ("Treinamento concluído!")

bestFit = p.bestFit()
print (f"Melhor opção: {bestFit}")

while g.loop():
    word = g.input()
    print (p.entropy[word])
