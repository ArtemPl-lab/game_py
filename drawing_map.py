from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication,QLabel)

def draw_map(grid,sprite):
        my_thread = Thread_draw(grid,sprite)
        my_thread.start()