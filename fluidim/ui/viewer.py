from loguru import logger
from PySide6.QtWidgets import QSizePolicy, QStackedWidget


class Viewer(QStackedWidget):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "Viewer"')

        self.func_atualizar = func_atualizar

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "Viewer.atualizar"')
