from PyQt5.QtWidgets import QFileDialog
from .UI.ui_main import Ui_MainWindow
import DataHandler.Reader as FileReader
import DataHandler.Generator as Generator
import Network.NeuralNetwork as nn

class MainWindowSlots(Ui_MainWindow):
    def __init__(self):
        self.k1 = []
        self.k2 = []

        self.ours_path = []
        self.ours = []

        self.aliens_path = []
        self.aliens = []

        self.network = None

    def k1_load(self):
        self.k1 = self.__k_load(FileReader.read_k1)

    def k1_gen(self):
        self.k1 = Generator.generate_k1(320)

    def k2_load(self):
        self.k2 = self.__k_load(FileReader.read_k2)

    def k2_gen(self):
        self.k2 = Generator.generate_k2(256)

    def ours_load(self):
        self.ours_paths = self.__openFileNamesDialog("Ours files (*.txt)")

    def aliens_load(self):
        self.aliens_paths = self.__openFileNamesDialog("Aliens files (*.txt)")

    def learn_network(self):
        count_neurons1 = self.count_neurons_l1_spinbox.value()
        count_neurons2 = self.count_neurons_l2_spinbox.value()

        count_inputs_n1 = self.neuron_l1_count_inputs_spinbox.value()
        count_component_input_n1 = self.neuron_l1_count_input_components_spinbox.value()
        count_inputs_n2 = self.neuron_l2_count_inputs_spinbox.value()

        self.ours = FileReader.read_matrix_files(self.ours_path, count_inputs_n1, count_component_input_n1)
        self.aliens = FileReader.read_matrix_files(self.aliens_path,  count_inputs_n1, count_component_input_n1)

        self.network = nn.NeuralNetwork(h=count_inputs_n1, g=count_inputs_n2, 
            components=count_component_input_n1, n1=count_neurons1, n2=count_neurons2)

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
