import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Game_Thread
import generate_map
import player
import random
from PyQt5.QtCore import *
class Game_widget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

    def keyPressEvent(self, event):
        key = event.key()
        if key == 16777234:            #left
            player1.go_left()
            player1.isTeleported(tp)
        elif key == 16777236:            #right
            player1.go_right()
            player1.isTeleported(tp)
        elif key == 16777235:            #up
            player1.go_up()
            player1.isTeleported(tp)

        elif key == 16777237:            #down
            player1.go_down()
            player1.isTeleported(tp)
        elif key == 16777267:            #draw_line
            player1.draw_line(True)
        elif key == 16777268:            #undraw line
            player1.draw_line(False)
        else:
            print(key)
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
    tl = QPixmap('portal.png')
    for i in range(20):
        tp_start = random.randint(0, len(pl_pos_mass) - 1)
        tp_end = random.randint(0, len(pl_pos_mass) - 1)
        tp_start_pos = pl_pos_mass[tp_start]
        tp_end_pos = pl_pos_mass[tp_end]
        if tp_start_pos != tp_end_pos:
            tp.append([tp_start_pos,tp_end_pos])
            l = QLabel()
            l.setPixmap(tl)
            grid.addWidget(l,tp_start_pos[1],tp_start_pos[0])
            print(tp[len(tp)-1])
    player1.update()
def draw_map(map1):
    thread, thread2, thread3 = Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread()
    thread.output[int, int,int].connect(create_lb)
    thread2.output[int, int,int].connect(create_lb)
    thread3.output[int, int,int].connect(create_lb)
    thread.render(0, 0, h+1, 3,map1)
    thread2.render(0, 3, h+1, wh//2,map1)
    thread3.render(0, wh//2, h+1, wh + 1,map1)
    thread3.finished.connect(playing)
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
    pl_pos_mass = generate_map.generate_lab(map_)

    ran = random.randint(0, (len(pl_pos_mass) - 1)//2)
    start_pos_pl = pl_pos_mass[ran]
    ran2 = random.randint((len(pl_pos_mass) - 1)//2, len(pl_pos_mass) - 1)
    finish_pos_pl = pl_pos_mass[ran2]
    pc = QPixmap('player.png')
    player1 = player.player(grid,map_,start_pos_pl,finish_pos_pl,pc)
    tp = []
    draw_map(map_)


    sys.exit(app.exec_())