import pickle

from loguru import logger


class Sistema:
    def __init__(self):
        logger.log('CLASS', 'Criando classe "Sistema"')

        self.circuito = Circuito()
        self.caminho = None

    def novo(self):
        self.caminho = None
        self.circuito = Circuito()

    def salvar(self):
        if self.caminho is not None:
            with open(self.caminho, 'wb') as arq:
                pickle.dump(self.circuito, arq)

    def salvar_como(self, caminho):
        self.caminho = caminho
        self.salvar()

    def abrir(self, caminho):
        self.caminho = caminho
        with open(caminho, 'rb') as arq:
            self.circuito = pickle.load(arq)


class Circuito:
    def __init__(self):
        logger.log('CLASS', 'Criando classe "Circuito"')

        self.nos = []
        self.trechos = []


sistema = Sistema()
