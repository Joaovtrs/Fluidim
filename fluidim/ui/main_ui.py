from loguru import logger
from PySide6.QtWidgets import QMainWindow
from sistema import sistema

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

        if sistema.caminho is not None:
            logger.debug('Atualização da janela com o caminho do arquivo')
            arquivo = str(sistema.caminho).split('/')[-1]
            self.setWindowTitle('Fluidim: ' + str(arquivo))
        else:
            logger.debug('Atualização da janela sem o caminho do arquivo')
            self.setWindowTitle('Fluidim')

        self.menu_bar.atualizar()
