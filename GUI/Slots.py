import json
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
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
        self.k1_status_label.setText('+')

    def k1_gen(self):
        self.k1 = Generator.generate_k1(320)
        self.k1_status_label.setText('+')

    def k2_load(self):
        self.k2 = self.__k_load(FileReader.read_k2)
        self.k2_status_label.setText('+')

    def k2_gen(self):
        self.k2 = Generator.generate_k2(256)
        self.k2_status_label.setText('+')

    def ours_load(self):
        self.ours_paths = self.__openFileNamesDialog("Ours files (*.txt)")
        self.ours_status_label.setText('+')

    def aliens_load(self):
        self.aliens_paths = self.__openFileNamesDialog("Aliens files (*.txt)")
        self.aliens_status_label.setText('+')

    def learn_network(self):
        count_neurons1 = self.count_neurons_l1_spinbox.value()
        count_neurons2 = self.count_neurons_l2_spinbox.value()

        count_inputs_n1 = self.neuron_l1_count_inputs_spinbox.value()
        count_component_input_n1 = self.neuron_l1_count_input_components_spinbox.value()
        count_inputs_n2 = self.neuron_l2_count_inputs_spinbox.value()

        self.ours = FileReader.read_matrix_files(self.ours_paths, count_inputs_n1, count_component_input_n1)
        self.aliens = FileReader.read_matrix_files(self.aliens_paths,  count_inputs_n1, count_component_input_n1)

        self.network = nn.NeuralNetwork(h=count_inputs_n1, g=count_inputs_n2, 
            components=count_component_input_n1, n1=count_neurons1, n2=count_neurons2)

        self.network.learn(self.k1, self.k2, self.ours, self.aliens)

        QMessageBox.about(None, "Learn neural network", "Done!")

    def export_network(self):
        fileName = self.__saveFileDialog("Network config file (*.json)")

        if fileName:
            with open(fileName, 'w') as file_out:
                dict_vals = self.network.__dict__
                dict_vals['w'] = dict_vals['w'].tolist()
                dict_vals['mu'] = dict_vals['mu'].tolist()
                dict_vals['W'] = dict_vals['W'].tolist()
                dict_vals['signs_w'] = [sig.tolist() for sig in dict_vals['signs_w']]
                
                json_obj = json.dumps(dict_vals, indent=4)
                print(json_obj, file=file_out)

            QMessageBox.about(None, "Saving neural network", "Done!")

    def load_network(self):
        fileName = self.__openFileNameDialog("Network config file (*.json)")

        if fileName:
            with open(fileName, 'r') as file_in:
                file_text = file_in.read()
                json_obj = json.loads(file_text)
                json_obj['mu'] = np.array(json_obj['mu'])
                json_obj['W'] = np.array(json_obj['W'])

                self.network = nn.NeuralNetwork()
                self.network.__dict__ = json_obj

            QMessageBox.about(None, "Loading neural network", "Done!")

    def test_network(self):
        n_el = self.neuron_l1_count_inputs_spinbox.value()
        m_com = self.neuron_l1_count_input_components_spinbox.value()
        form_file = self.__openFileNameDialog("Test form file (*.txt)")
        form = FileReader.read_matrix_file(form_file, n_el, m_com)

        res_key = self.network.get_key(form)
        diff = 0

        for i in range(len(res_key)):
            diff += 1 if res_key[i] != self.k2[i] else 0

        QMessageBox.about(None, "Test neural network", "Done! Diff: " + str(diff))


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

    def __saveFileDialog(self, file_types):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,
            "QFileDialog.getSaveFileName()","",file_types, options=options)
        
        return fileName
