from .Slots import MainWindowSlots

class MainWindow(MainWindowSlots):
    def __init__(self, form):
        self.setupUi(form)
        self.connect_slots()

    def connect_slots(self):
        self.k1_load_btn.clicked.connect(self.k1_load)
        self.k1_gen_btn.clicked.connect(self.k1_gen)
        self.k2_load_btn.clicked.connect(self.k2_load)
        self.k2_gen_btn.clicked.connect(self.k2_gen)
        self.ours_load_btn.clicked.connect(self.ours_load)
        self.aliens_load_btn.clicked.connect(self.aliens_load)
        self.learn_btn.clicked.connect(self.learn_network)
