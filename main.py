import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    window.setStyleSheet(open("style.qss", "r").read())
    w.showFullScreen()

    sys.exit(app.exec_())