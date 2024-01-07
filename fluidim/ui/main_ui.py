from loguru import logger
from PySide6.QtWidgets import QMainWindow


class MainUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainUI"')

        self.resize(800, 600)
        self.setWindowTitle('Fluidim')
        self.setMinimumSize(800, 600)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "MainUI.atualizar"')
