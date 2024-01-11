from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from sistema import sistema


class ViewTrechos(QFrame):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ViewTrechos"')

        self.func_atualizar = func_atualizar

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.lbl_titulo = QLabel('Trechos')
        self.lbl_titulo.setAlignment(Qt.AlignHCenter)
        self.lbl_titulo.setFont(QFont('Times', 20))

        self.separdor_titulo = QFrame(self)
        self.separdor_titulo.setFrameShape(QFrame.HLine)

        self.grid.addWidget(self.lbl_titulo)
        self.grid.addWidget(self.separdor_titulo)

    @staticmethod
    def atualizar():
        logger.log('METHOD', 'Chamando função "ViewTrechos.atualizar"')
