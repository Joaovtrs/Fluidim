import pickle

from loguru import logger

from .nos import No
from .trechos import Trecho


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

    def add_no(self):
        self.nos.append(No('n'))

    def add_trecho(self):
        self.trechos.append(Trecho())

    def get_nos(self):
        resposta = []

        for no in self.nos:
            resposta.append({
                'nome': no.nome,
                'conta': no.cota,
                'pressao': no.pressao
            })

        resposta.sort(key=lambda x: x['nome'])

        return resposta

    def get_trechos(self):
        resposta = []

        for trecho in self.trechos:
            resposta.append({
                'nome': trecho.get_nome(),
                'diametro': trecho.diametro,
                'comprimento': trecho.comprimento,
                'vazao': trecho.vazao,
                'montante': trecho.no_montante,
                'jusante': trecho.no_jusante
            })

        resposta.sort(key=lambda x: x['nome'])

        return resposta


sistema = Sistema()
