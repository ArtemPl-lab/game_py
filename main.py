import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import Game_Thread
import generate_map
import player
import time
class Game_widget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

    def keyPressEvent(self, event):
        key = event.key()
        if key == 16777234:
            player1.go_left()
            print("Left")
        elif key == 16777236:
            player1.go_right()
            print("Right")
        elif key == 16777235:
            player1.go_up()
            print("Up")
        elif key == 16777237:
            player1.go_down()
            print("Down")

        elif key == 16777267:
            player1.draw_line(True)
        elif key == 16777268:
            player1.draw_line(False)
def create_lb(i,j,block):
    label = QLabel()
    pic = QPixmap()
    if block == 3:
        pic = QPixmap('sprite.jpg__resize_sprite.png')
    elif block == 0 or block == 1:
        pic =  QPixmap('sprite.jpg__resize_sprite2.png')
    label.setPixmap(pic)
    grid.addWidget(label,i,j)
def playing():
    player1.update()
if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = Game_widget()
    w.setWindowTitle('Game')
    w.setStyleSheet(open("style.qss", "r").read())
    w.showFullScreen()
    h = w.frameSize().height()//16
    wh = w.frameSize().width()//16
    #img = crop('./sprite.jpg', (1081, 70, 1097, 86))
    #image = QPixmap(img)
    grid = QGridLayout()
    grid.setSpacing(0)
    grid.setContentsMargins(0, 0, 0, 0)
    w.setLayout(grid)

    map_ =  generate_map.generate_mass(h,wh)
    generate_map.generate_lab(map_)

    pc = QPixmap('player.png')
    player1 = player.player(grid,map_,pc)


    thread, thread2, thread3 = Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread()
    thread.output[int, int,int].connect(create_lb)
    thread2.output[int, int,int].connect(create_lb)
    thread3.output[int, int,int].connect(create_lb)
    thread.render(0, 0, h+1, 3,map_)
    thread2.render(0, 3, h+1, wh//2,map_)
    thread3.render(0, wh//2, h+1, wh + 1,map_)
    thread3.finished.connect(playing)
    sys.exit(app.exec_())