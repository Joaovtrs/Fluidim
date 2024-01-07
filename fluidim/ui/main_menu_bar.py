import os

from loguru import logger
from PySide6.QtWidgets import QFileDialog, QMenuBar

from sistema import sistema

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                       'OneDrive\\Área de Trabalho')


class MainMenuBar(QMenuBar):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainMenuBar"')

        self.func_atualizar = func_atualizar

        self.arquivo = self.addMenu('Arquivo')

        self.arq_novo = self.arquivo.addAction('Novo projeto')
        self.arq_novo.setShortcut('Ctrl+N')

        self.arq_abrir = self.arquivo.addAction('Abrir projeto')
        self.arq_abrir.setShortcut('Ctrl+O')

        self.arquivo.addSeparator()

        self.arq_salvar = self.arquivo.addAction('Salvar projeto')
        self.arq_salvar.setShortcut('Ctrl+S')

        self.arq_salvar_como = self.arquivo.addAction('Salvar projeto como')
        self.arq_salvar_como.setShortcut('Ctrl+Shift+S')

        self.arq_novo.triggered.connect(self.func_arq_novo)
        self.arq_abrir.triggered.connect(self.func_arq_abrir)
        self.arq_salvar.triggered.connect(self.func_arq_salvar)
        self.arq_salvar_como.triggered.connect(self.func_arq_salvar_como)

    @staticmethod
    def atualizar():
        logger.log('METHOD', 'Chamando função "MainMenuBar.atualizar"')

    @staticmethod
    def func_arq_novo():
        logger.log('METHOD', 'Chamando função "MainMenuBar.func_arq_novo"')

        sistema.novo()

    def func_arq_salvar(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.func_arq_salvar"')

        if sistema.caminho is not None:
            sistema.salvar()
        else:
            self.func_arq_salvar_como()

    def func_arq_salvar_como(self):
        logger.log(
            'METHOD',
            'Chamando função "MainMenuBar.func_arq_salvar_como"'
        )

        caminho = QFileDialog.getSaveFileName(
            parent=self,
            caption='Salvar como',
            filter='*.fluid',
            dir=desktop
        )

        if caminho[0]:
            sistema.salvar_como(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Nenhum caminho selecionado')

    def func_arq_abrir(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.func_arq_abrir"')

        caminho = QFileDialog.getOpenFileName(
            parent=self,
            caption='Abrir',
            filter='*.fluid',
            dir=desktop
        )

        if caminho[0]:
            sistema.abrir(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Nenhum caminho selecionado')
