from loguru import logger
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout

from .main_menu_buttons import MainManuButton


class MainMenu(QFrame):
    def __init__(self, viewer, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainMenu"')

        self.viewer = viewer

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(80)
        self.setMaximumWidth(80)

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.btn_menu = MainManuButton(' Menu', 'icons/menu.png', self)

        self.separador = QFrame(self)
        self.separador.setFrameShape(QFrame.HLine)

        self.btn_conexoes = MainManuButton(
            ' Conexões',
            'icons/connection.png',
            self
        )
        self.btn_trechos = MainManuButton(
            ' Trechos',
            'icons/algorithm.png',
            self
        )

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )

        self.grid.addWidget(self.btn_menu)
        self.grid.addWidget(self.separador)
        self.grid.addWidget(self.btn_conexoes)
        self.grid.addWidget(self.btn_trechos)
        self.grid.addItem(self.spacer)

        self.btn_menu.clicked.connect(self.func_btn_menu)
        self.btn_conexoes.clicked.connect(
            lambda: self.viewer.setCurrentWidget(self.viewer.view_conexoes)
        )
        self.btn_trechos.clicked.connect(
            lambda: self.viewer.setCurrentWidget(self.viewer.view_trechos)
        )

    def func_btn_menu(self):
        logger.log('METHOD', 'Chamando função "MainMenu.func_btn_menu"')

        anim_max = QPropertyAnimation(self, b'maximumWidth', self)
        anim_min = QPropertyAnimation(self, b'minimumWidth', self)
        anim_max.setDuration(100)
        anim_min.setDuration(100)

        if self.width() == 80:
            logger.debug('Abrindo menu')
            anim_max.setStartValue(80)
            anim_min.setStartValue(80)
            anim_max.setEndValue(200)
            anim_min.setEndValue(200)
            anim_max.start()
            anim_min.start()
        elif self.width() == 200:
            logger.debug('Fechando menu')
            anim_max.setStartValue(200)
            anim_min.setStartValue(200)
            anim_max.setEndValue(80)
            anim_min.setEndValue(80)
            anim_max.start()
            anim_min.start()
