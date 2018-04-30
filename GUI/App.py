from .Slots import MainWindowSlots

MAX_NEURONS = 1000
MAX_INPUTS = 1000
MAX_COMPONENTS = 1000

class MainWindow(MainWindowSlots):
    def __init__(self, form):
        self.setupUi(form)

        self.count_neurons_l1_spinbox.setMaximum(MAX_NEURONS)
        self.count_neurons_l2_spinbox.setMaximum(MAX_NEURONS)

        self.neuron_l1_count_inputs_spinbox.setMaximum(MAX_INPUTS)
        self.neuron_l1_count_input_components_spinbox.setMaximum(MAX_COMPONENTS)
        self.neuron_l2_count_inputs_spinbox.setMaximum(MAX_INPUTS)

        self.connect_slots()

    def connect_slots(self):
        self.k1_load_btn.clicked.connect(self.k1_load)
        self.k1_gen_btn.clicked.connect(self.k1_gen)
        self.k2_load_btn.clicked.connect(self.k2_load)
        self.k2_gen_btn.clicked.connect(self.k2_gen)
        self.ours_load_btn.clicked.connect(self.ours_load)
        self.aliens_load_btn.clicked.connect(self.aliens_load)
        self.learn_btn.clicked.connect(self.learn_network)
