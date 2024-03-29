from loguru import logger
from PySide6.QtWidgets import QSizePolicy, QStackedWidget

from .view_conexoes import ViewConexoes
from .view_trechos import ViewTrechos


class Viewer(QStackedWidget):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "Viewer"')

        self.func_atualizar = func_atualizar

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.view_conexoes = ViewConexoes(self.func_atualizar, self)
        self.view_trechos = ViewTrechos(self.func_atualizar, self)

        self.addWidget(self.view_conexoes)
        self.addWidget(self.view_trechos)

        self.currentChanged.connect(lambda *args: self.func_atualizar())

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "Viewer.atualizar"')

        self.view_conexoes.atualizar()
