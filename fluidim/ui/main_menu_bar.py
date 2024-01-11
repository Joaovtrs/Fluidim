import os

from loguru import logger
from PySide6.QtWidgets import QFileDialog, QMenuBar, QMessageBox
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

    def pop_up(self, texto):
        logger.log('METHOD', 'Chamando função "MainMenuBar.pop_up"')

        pop_up_excluir = QMessageBox(self)
        pop_up_excluir.setWindowTitle('Aviso')
        pop_up_excluir.setText(texto)
        pop_up_excluir.setInformativeText(
            'Todas as alterações não salvas serão perdidas'
        )
        pop_up_excluir.setIcon(QMessageBox.Warning)
        pop_up_excluir.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        pop_up_excluir.setButtonText(QMessageBox.No, 'Não')
        pop_up_excluir.setButtonText(QMessageBox.Yes, 'Sim')
        pop_up_excluir.setDefaultButton(QMessageBox.No)

        return pop_up_excluir.exec()

    def func_arq_novo(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.func_arq_novo"')

        resp = self.pop_up('Deseja criar um novo arquivo?')

        if resp == QMessageBox.Yes:
            sistema.novo()
            self.func_atualizar()

    def func_arq_salvar(self):
        logger.log('METHOD', 'Chamando função "MainMenuBar.func_arq_salvar"')

        if sistema.caminho is not None:
            sistema.salvar()
            self.func_atualizar()
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

        resp = self.pop_up('Deseja abrir outro arquivo?')

        if resp == QMessageBox.Yes:
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
