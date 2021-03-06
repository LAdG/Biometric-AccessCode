# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Resource/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.learn_box = QtWidgets.QGroupBox(self.centralwidget)
        self.learn_box.setObjectName("learn_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.learn_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.config_box = QtWidgets.QGroupBox(self.learn_box)
        self.config_box.setObjectName("config_box")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.config_box)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.count_neurons_label_layout = QtWidgets.QHBoxLayout()
        self.count_neurons_label_layout.setObjectName("count_neurons_label_layout")
        self.count_neurons_l1_label = QtWidgets.QLabel(self.config_box)
        self.count_neurons_l1_label.setObjectName("count_neurons_l1_label")
        self.count_neurons_label_layout.addWidget(self.count_neurons_l1_label)
        self.count_neurons_l2_label = QtWidgets.QLabel(self.config_box)
        self.count_neurons_l2_label.setObjectName("count_neurons_l2_label")
        self.count_neurons_label_layout.addWidget(self.count_neurons_l2_label)
        self.verticalLayout_8.addLayout(self.count_neurons_label_layout)
        self.count_neurons_layout = QtWidgets.QHBoxLayout()
        self.count_neurons_layout.setObjectName("count_neurons_layout")
        self.count_neurons_l1_spinbox = QtWidgets.QSpinBox(self.config_box)
        self.count_neurons_l1_spinbox.setObjectName("count_neurons_l1_spinbox")
        self.count_neurons_layout.addWidget(self.count_neurons_l1_spinbox)
        self.count_neurons_l2_spinbox = QtWidgets.QSpinBox(self.config_box)
        self.count_neurons_l2_spinbox.setObjectName("count_neurons_l2_spinbox")
        self.count_neurons_layout.addWidget(self.count_neurons_l2_spinbox)
        self.verticalLayout_8.addLayout(self.count_neurons_layout)
        self.neurons_input_config_label_layout = QtWidgets.QHBoxLayout()
        self.neurons_input_config_label_layout.setObjectName("neurons_input_config_label_layout")
        self.neuron_l1_count_inputs_label = QtWidgets.QLabel(self.config_box)
        self.neuron_l1_count_inputs_label.setObjectName("neuron_l1_count_inputs_label")
        self.neurons_input_config_label_layout.addWidget(self.neuron_l1_count_inputs_label)
        self.neuron_l1_count_input_components_label = QtWidgets.QLabel(self.config_box)
        self.neuron_l1_count_input_components_label.setObjectName("neuron_l1_count_input_components_label")
        self.neurons_input_config_label_layout.addWidget(self.neuron_l1_count_input_components_label)
        self.neuron_l2_count_inputs_label = QtWidgets.QLabel(self.config_box)
        self.neuron_l2_count_inputs_label.setObjectName("neuron_l2_count_inputs_label")
        self.neurons_input_config_label_layout.addWidget(self.neuron_l2_count_inputs_label)
        self.verticalLayout_8.addLayout(self.neurons_input_config_label_layout)
        self.neurons_input_config_layout = QtWidgets.QHBoxLayout()
        self.neurons_input_config_layout.setObjectName("neurons_input_config_layout")
        self.neuron_l1_count_inputs_spinbox = QtWidgets.QSpinBox(self.config_box)
        self.neuron_l1_count_inputs_spinbox.setObjectName("neuron_l1_count_inputs_spinbox")
        self.neurons_input_config_layout.addWidget(self.neuron_l1_count_inputs_spinbox)
        self.neuron_l1_count_input_components_spinbox = QtWidgets.QSpinBox(self.config_box)
        self.neuron_l1_count_input_components_spinbox.setObjectName("neuron_l1_count_input_components_spinbox")
        self.neurons_input_config_layout.addWidget(self.neuron_l1_count_input_components_spinbox)
        self.neuron_l2_count_inputs_spinbox = QtWidgets.QSpinBox(self.config_box)
        self.neuron_l2_count_inputs_spinbox.setObjectName("neuron_l2_count_inputs_spinbox")
        self.neurons_input_config_layout.addWidget(self.neuron_l2_count_inputs_spinbox)
        self.verticalLayout_8.addLayout(self.neurons_input_config_layout)
        self.verticalLayout_3.addWidget(self.config_box)
        self.k1_layout = QtWidgets.QHBoxLayout()
        self.k1_layout.setObjectName("k1_layout")
        self.k1_label = QtWidgets.QLabel(self.learn_box)
        self.k1_label.setObjectName("k1_label")
        self.k1_layout.addWidget(self.k1_label)
        self.k1_status_label = QtWidgets.QLabel(self.learn_box)
        self.k1_status_label.setObjectName("k1_status_label")
        self.k1_layout.addWidget(self.k1_status_label)
        self.k1_load_btn = QtWidgets.QPushButton(self.learn_box)
        self.k1_load_btn.setObjectName("k1_load_btn")
        self.k1_layout.addWidget(self.k1_load_btn)
        self.k1_gen_btn = QtWidgets.QPushButton(self.learn_box)
        self.k1_gen_btn.setObjectName("k1_gen_btn")
        self.k1_layout.addWidget(self.k1_gen_btn)
        self.verticalLayout_3.addLayout(self.k1_layout)
        self.k2_layout = QtWidgets.QHBoxLayout()
        self.k2_layout.setObjectName("k2_layout")
        self.k2_label = QtWidgets.QLabel(self.learn_box)
        self.k2_label.setObjectName("k2_label")
        self.k2_layout.addWidget(self.k2_label)
        self.k2_status_label = QtWidgets.QLabel(self.learn_box)
        self.k2_status_label.setObjectName("k2_status_label")
        self.k2_layout.addWidget(self.k2_status_label)
        self.k2_load_btn = QtWidgets.QPushButton(self.learn_box)
        self.k2_load_btn.setObjectName("k2_load_btn")
        self.k2_layout.addWidget(self.k2_load_btn)
        self.k2_gen_btn = QtWidgets.QPushButton(self.learn_box)
        self.k2_gen_btn.setObjectName("k2_gen_btn")
        self.k2_layout.addWidget(self.k2_gen_btn)
        self.k2_save_btn = QtWidgets.QPushButton(self.learn_box)
        self.k2_save_btn.setObjectName("k2_save_btn")
        self.k2_layout.addWidget(self.k2_save_btn)
        self.verticalLayout_3.addLayout(self.k2_layout)
        self.ours_layout = QtWidgets.QHBoxLayout()
        self.ours_layout.setObjectName("ours_layout")
        self.ours_label = QtWidgets.QLabel(self.learn_box)
        self.ours_label.setObjectName("ours_label")
        self.ours_layout.addWidget(self.ours_label)
        self.ours_status_label = QtWidgets.QLabel(self.learn_box)
        self.ours_status_label.setObjectName("ours_status_label")
        self.ours_layout.addWidget(self.ours_status_label)
        self.ours_load_btn = QtWidgets.QPushButton(self.learn_box)
        self.ours_load_btn.setObjectName("ours_load_btn")
        self.ours_layout.addWidget(self.ours_load_btn)
        self.verticalLayout_3.addLayout(self.ours_layout)
        self.aliens_layout = QtWidgets.QHBoxLayout()
        self.aliens_layout.setObjectName("aliens_layout")
        self.aliens_label = QtWidgets.QLabel(self.learn_box)
        self.aliens_label.setObjectName("aliens_label")
        self.aliens_layout.addWidget(self.aliens_label)
        self.aliens_status_label = QtWidgets.QLabel(self.learn_box)
        self.aliens_status_label.setObjectName("aliens_status_label")
        self.aliens_layout.addWidget(self.aliens_status_label)
        self.aliens_load_btn = QtWidgets.QPushButton(self.learn_box)
        self.aliens_load_btn.setObjectName("aliens_load_btn")
        self.aliens_layout.addWidget(self.aliens_load_btn)
        self.verticalLayout_3.addLayout(self.aliens_layout)
        self.learn_btn = QtWidgets.QPushButton(self.learn_box)
        self.learn_btn.setObjectName("learn_btn")
        self.verticalLayout_3.addWidget(self.learn_btn)
        self.verticalLayout_2.addWidget(self.learn_box)
        self.load_box = QtWidgets.QGroupBox(self.centralwidget)
        self.load_box.setObjectName("load_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.load_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.network_layout = QtWidgets.QHBoxLayout()
        self.network_layout.setObjectName("network_layout")
        self.network_label = QtWidgets.QLabel(self.load_box)
        self.network_label.setObjectName("network_label")
        self.network_layout.addWidget(self.network_label)
        self.network_status_label = QtWidgets.QLabel(self.load_box)
        self.network_status_label.setObjectName("network_status_label")
        self.network_layout.addWidget(self.network_status_label)
        self.network_export_btn = QtWidgets.QPushButton(self.load_box)
        self.network_export_btn.setObjectName("network_export_btn")
        self.network_layout.addWidget(self.network_export_btn)
        self.network_load_btn = QtWidgets.QPushButton(self.load_box)
        self.network_load_btn.setObjectName("network_load_btn")
        self.network_layout.addWidget(self.network_load_btn)
        self.verticalLayout_4.addLayout(self.network_layout)
        self.verticalLayout_2.addWidget(self.load_box)
        self.test_box = QtWidgets.QGroupBox(self.centralwidget)
        self.test_box.setObjectName("test_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.test_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.testdata_layout = QtWidgets.QHBoxLayout()
        self.testdata_layout.setObjectName("testdata_layout")
        self.testdata_label = QtWidgets.QLabel(self.test_box)
        self.testdata_label.setObjectName("testdata_label")
        self.testdata_layout.addWidget(self.testdata_label)
        self.testdata_status_label = QtWidgets.QLabel(self.test_box)
        self.testdata_status_label.setObjectName("testdata_status_label")
        self.testdata_layout.addWidget(self.testdata_status_label)
        self.testdata_load_btn = QtWidgets.QPushButton(self.test_box)
        self.testdata_load_btn.setObjectName("testdata_load_btn")
        self.testdata_layout.addWidget(self.testdata_load_btn)
        self.verticalLayout_5.addLayout(self.testdata_layout)
        self.verticalLayout_2.addWidget(self.test_box)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Biometric-AccessCode"))
        self.learn_box.setTitle(_translate("MainWindow", "Learn neural network"))
        self.config_box.setTitle(_translate("MainWindow", "Neural network config"))
        self.count_neurons_l1_label.setText(_translate("MainWindow", "Count neurons in layer #1"))
        self.count_neurons_l2_label.setText(_translate("MainWindow", "Count  neurons in layer #2"))
        self.neuron_l1_count_inputs_label.setText(_translate("MainWindow", "Count neuron inputs in layer #1"))
        self.neuron_l1_count_input_components_label.setText(_translate("MainWindow", "Count neron input components in layer #1"))
        self.neuron_l2_count_inputs_label.setText(_translate("MainWindow", "Count neuron inputs in layer #2"))
        self.k1_label.setText(_translate("MainWindow", "k1"))
        self.k1_status_label.setText(_translate("MainWindow", "-"))
        self.k1_load_btn.setText(_translate("MainWindow", "Load"))
        self.k1_gen_btn.setText(_translate("MainWindow", "Generate"))
        self.k2_label.setText(_translate("MainWindow", "k2"))
        self.k2_status_label.setText(_translate("MainWindow", "-"))
        self.k2_load_btn.setText(_translate("MainWindow", "Load"))
        self.k2_gen_btn.setText(_translate("MainWindow", "Generate"))
        self.k2_save_btn.setText(_translate("MainWindow", "Save"))
        self.ours_label.setText(_translate("MainWindow", "Ours"))
        self.ours_status_label.setText(_translate("MainWindow", "-"))
        self.ours_load_btn.setText(_translate("MainWindow", "Load"))
        self.aliens_label.setText(_translate("MainWindow", "Aliens"))
        self.aliens_status_label.setText(_translate("MainWindow", "-"))
        self.aliens_load_btn.setText(_translate("MainWindow", "Load"))
        self.learn_btn.setText(_translate("MainWindow", "Learn"))
        self.load_box.setTitle(_translate("MainWindow", "Load neural network"))
        self.network_label.setText(_translate("MainWindow", "Network"))
        self.network_status_label.setText(_translate("MainWindow", "-"))
        self.network_export_btn.setText(_translate("MainWindow", "Export"))
        self.network_load_btn.setText(_translate("MainWindow", "Load"))
        self.test_box.setTitle(_translate("MainWindow", "Test neural network"))
        self.testdata_label.setText(_translate("MainWindow", "Test data"))
        self.testdata_status_label.setText(_translate("MainWindow", "-"))
        self.testdata_load_btn.setText(_translate("MainWindow", "Load"))

