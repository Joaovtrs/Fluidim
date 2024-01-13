class Trecho:
    def __init__(self):
        self.diametro = 0
        self.comprimento = 0
        self.vazao = 0

        self.no_montante = None
        self.no_jusante = None

    def get_nome(self):
        if self.no_jusante is None or self.no_montante is None:
            return ''
        else:
            return f'{self.no_montante.nome}-{self.no_jusante.nome}'
