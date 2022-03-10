from dataset.manipulate import WordList
import re

class Game:
    """ Classe responsável pela emulação do jogo. """

    def __init__(self, path="dataset/words.csv", maxRounds=6):
        self.wl = WordList(path)
        self.maxRounds = maxRounds
        self.newTurn()

    def __repr__(self):
        fmtd = ["".join(guess) for guess in self.guesses]
        return "\n".join(fmtd)

    def newTurn(self):
        """ Inicialização de uma nova rodada. Zera valores e escolhe palavra aleatória. """
        self.word = self.wl.getRandom()
        self.round = 1
        self.guesses = []

    def guess(self, word):
        """ Processa uma tentativa. Retorna string de resultado, com a letra
            B indicando uma letra ausente na palavra-chave, Y com uma letra
            presente, mas no local incorreto e G com uma letra no local correto. """
        self.round += 1
        result = ["B"] * 5
        # TODO: "oeste" gera 1 "Y" extra em "marte" com a letra "E".
        for i, letter in enumerate(word):
            if letter in self.word:
                result[i] = "Y"
            if letter == self.word[i]:
                result[i] = "G"
        # Processa para string:
        self.guesses.append(result)
        return "".join(result)

    def input(self):
        """ Valida a entrada de dados do usuário. Deve ser uma palavra de exatas
            cinco letras, maiúsculas ou minúsculas. Não são permitidos acentos ou
            números. """
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
        """ Condições para a continuação do jogo. Retorna True se o jogo deve continuar e False
            caso o jogo tenha terminado (por acerto ou fim do máximo de tentativas). """
        conditions = ['G'] * 5 in self.guesses
        conditions = conditions or (self.round > self.maxRounds)
        return not conditions
