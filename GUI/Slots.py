from .UI.ui_main import Ui_MainWindow

class MainWindowSlots(Ui_MainWindow):
    def set_btn_text(self):
        self.hello_btn.setText('Hello World!!!')
        return None
