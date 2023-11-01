from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from interface import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.objeto.signal.conect(self.slot)
        self.ui.pushButtonSelecionePasta.clicked.connect(self.seleciona_pasta)
        self.ui.pushButtonBaixar.clicked.connect(self.baixa_video)
        self.ui.pushButtonSelecioneArquivo.clicked.connect(self.seleciona_arquivo)
        self.ui.pushButtonTranscrever.clicked.connect(self.transcreve_audio)
        self.ui.pushButtonTraduzir.clicked.connect(self.traduz_audio)

    def seleciona_pasta(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            selected_directory = dialog.selectedFiles()
            print(f"Pasta selecionada: {selected_directory[0]}")

    def seleciona_arquivo(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if dialog.exec():
            selected_files = dialog.selectedFiles()
            print(f"Arquivo selecionado: {selected_files[0]}")

    def baixa_video(self):
        link = self.ui.lineEditLink.text()
        print(f"Link selecionado: {link}")

    def transcreve_audio(self):
        import whisper
        modelo = whisper.load_model("base")
        resposta = modelo.transcribe("audiencia_105554314_1_V.asf")
        print (resposta['text'])
            
    def traduz_audio(self):
        print('Ok 02')
        pass


if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()