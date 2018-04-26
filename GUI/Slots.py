from PyQt5.QtWidgets import QFileDialog
from .UI.ui_main import Ui_MainWindow

class MainWindowSlots(Ui_MainWindow):
    def __init__(self):
        self.k1 = ''
        self.k2 = ''

        self.ours_path = []
        self.ours = []

        self.aliens_path = []
        self.aliens = []

    def k1_load(self):
        k1_path = self.__openFileNameDialog("k1 file (*.txt)")

    def k2_load(self):
        k2_path = self.__openFileNameDialog("k2 file (*.txt)")

    def ours_load(self):
        ours_paths = self.__openFileNamesDialog("Matlab files (*.mat)")

    def aliens_load(self):
        aliens_paths = self.__openFileNamesDialog("Matlab files (*.mat)")

    def learn_network(self):
        pass

    def __openFileNameDialog(self, file_types):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,
            "QFileDialog.getOpenFileName()", "", file_types, options=options)
        
        return fileName

    def __openFileNamesDialog(self, file_types):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(None,
            "QFileDialog.getOpenFileNames()", "", file_types, options=options)

        return files
