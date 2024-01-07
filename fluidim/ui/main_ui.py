from loguru import logger
from PySide6.QtWidgets import QMainWindow

from .main_menu_bar import MainMenuBar


class MainUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainUI"')

        self.resize(800, 600)
        self.setWindowTitle('Fluidim')
        self.setMinimumSize(800, 600)

        self.menu_bar = MainMenuBar(self.atualizar, self)
        self.setMenuBar(self.menu_bar)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "MainUI.atualizar"')

        self.menu_bar.atualizar()
