import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QGridLayout,QLabel)
TIME_LIMIT = 100
class External(QThread):
    create_block = pyqtSignal(QLabel)
    def __init__(self,image):
        self.image = image
    def run(self):
        for i in range(50):
            for j in range(50):
                lb = QLabel()
                lb.setPixmap(self.image)
                self.create_block.emit(lb)
class Actions(QGridLayout):
    def __init__(self):
        super().__init__()
        self.show()
    def initialize(self):
        self.dr = External()
        self.dr.create_block.connect(self.onCountChanged)
    def start_draw(self):
        self.dr.start()
    def onCountChanged(self, value):
        self.addWidget(value)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())