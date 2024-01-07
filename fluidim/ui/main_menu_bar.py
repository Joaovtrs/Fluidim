import os

from loguru import logger
from PySide6.QtWidgets import QFileDialog, QMenuBar

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                       'OneDrive\\Área de Trabalho')


class MainMenuBar(QMenuBar):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainMenuBar"')

        self.func_atualizar = func_atualizar

        self.arquivo = self.addMenu('Arquivo')

        self.arq_novo = self.arquivo.addAction('Novo arquivo')
        self.arq_novo.setShortcut('Ctrl+N')

        self.arq_abrir = self.arquivo.addAction('Abrir arquivo')
        self.arq_abrir.setShortcut('Ctrl+O')

        self.arq_novo.triggered.connect(self.criar_arquivo)
        self.arq_abrir.triggered.connect(self.abrir_arquivo)

    @staticmethod
    def atualizar():
        logger.log('METHOD', 'Chamando função "MainMenuBar.atualizar"')

    def criar_arquivo(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.criar_arquivo"')

        caminho = QFileDialog.getSaveFileName(
            parent=self,
            caption='Salvar como',
            filter='*.fluid',
            dir=desktop
        )

        if caminho[0]:
            # sistema.criar_db(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Nenhum caminho selecionado')

    def abrir_arquivo(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.abrir_arquivo"')

        caminho = QFileDialog.getOpenFileName(
            parent=self,
            caption='Abrir',
            filter='*.fluid',
            dir=desktop
        )

        if caminho[0]:
            # sistema.abrir_db(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Nenhum caminho selecionado')
