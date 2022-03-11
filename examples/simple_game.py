# EXEMPLO DE JOGO:
from game import Game

game = Game()

while game.loop():
    word = game.input()
    game.guess(word)

    print (game)

print (f"Palavra: {game.word}\n")