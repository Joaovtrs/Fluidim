from loguru import logger


class Sistema:
    def __init__(self):
        logger.log('CLASS', 'Criando classe "Sistema"')

        self.circuito = Circuito()

    def novo_circuito(self):
        self.circuito = Circuito()


class Circuito:
    def __init__(self):
        logger.log('CLASS', 'Criando classe "Circuito"')

        self.nos = []
        self.trechos = []


sistema = Sistema()
