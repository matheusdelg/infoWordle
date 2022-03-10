from random import choice
import csv, unicodedata, re

class WordList:
    """ Classe responsável pelo processamento de lista de palavras. """
    DEFAULT_PATH = "dataset/words.csv"

    def __repr__(self):
        return str(self.wordlist)

    def __init__(self, path=None, delim=",", enc="utf-8"):
        self.wordlist = self.load(path, delim, enc)

    def load(self, path=None, delim=",", enc="utf-8"):
        """ Carrega informações de uma tabela .CSV. Caso não especificado, considera
            DEFAULT_PATH (base de dados completa). """
        if path is None:
            path = WordList.DEFAULT_PATH

        with open(path, encoding=enc) as f:
            reader = csv.reader(f, delimiter=delim)
            wordlist  = [self.normalize(word[0]) for word in reader]
            return wordlist

    def normalize(self, word):
        """ Converte a lista de palavras no padrão: sem acentos e com letras maiúsculas. """
        word = unicodedata.normalize("NFD", word).encode('ASCII', 'ignore').decode('utf-8')
        return str.upper(word)

    def getRandom(self):
        """ Seleciona uma amostra aleatória da lista. """
        return choice(self.wordlist)

    def filter(words, guess, result):
        """ Retorna uma lista de palavras compatível com o resultado obtido. """
        regex = WordList.setRegex(guess, result)
        return list(filter(regex.match, words))
    
    def setRegex(guess, result):
        """ Monta expressão regular com os dados informados. """
        regex = "^"; ahead = ""
        for k, match in enumerate(result):
            if match == "G":
                regex += guess[k]
            elif match == "Y":
                regex += "."
                ahead += f"(?=.*[{guess[k]}].*)"
            else:
                ahead += f"(?=.*[^{guess[k]}].*)"
                regex += "."
        regex += "$"
        return re.compile(ahead + regex)

