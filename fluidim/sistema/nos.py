class No:
    def __init__(self, nome):
        self.nome = nome

        self.cota = 0
        self.pressao = 0


class No2Conexoes(No):
    def __init__(self, nome):
        super().__init__(nome)
        self.conexao_1 = None
        self.conexao_2 = None

        self.comprimento_equivalente_1_2 = 0


class No3Conexoes(No):
    def __init__(self, nome):
        super().__init__(nome)
        self.conexao_1 = None
        self.conexao_2 = None
        self.conexao_3 = None

        self.comprimento_equivalente_1_2 = 0
        self.comprimento_equivalente_1_3 = 0
        self.comprimento_equivalente_2_3 = 0
