from .Slots import MainWindowSlots

class MainWindow(MainWindowSlots):
    def __init__(self, form):
        self.setupUi(form)
        self.connect_slots()

    def connect_slots(self):
        self.hello_btn.clicked.connect(self.set_btn_text)
        return None
