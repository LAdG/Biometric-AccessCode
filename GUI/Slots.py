from PyQt5.QtWidgets import QFileDialog
from .UI.ui_main import Ui_MainWindow
import DataHandler.Reader as FileReader

class MainWindowSlots(Ui_MainWindow):
    def __init__(self):
        self.k1 = []
        self.k2 = []

        self.ours_path = []
        self.ours = []

        self.aliens_path = []
        self.aliens = []

    def k1_load(self):
        self.k1 = self.__k_load(FileReader.read_k1)

    def k2_load(self):
        self.k2 = self.__k_load(FileReader.read_k2)

    def ours_load(self):
        ours_paths = self.__openFileNamesDialog("Matlab files (*.mat)")

    def aliens_load(self):
        aliens_paths = self.__openFileNamesDialog("Matlab files (*.mat)")

    def learn_network(self):
        pass

    def __k_load(self, reader):
        k_path = self.__openFileNameDialog("Key file (*.txt)")

        if len(k_path) == 0:
            return

        return reader(k_path)

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
