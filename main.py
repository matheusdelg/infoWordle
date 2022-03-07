
from game import Game

game = Game()

print (game.word)

while game.loop():
    word = game.input()
    game.guess(word)

    print (game)
