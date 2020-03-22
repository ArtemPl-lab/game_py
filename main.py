import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
import Game_Thread
import generate_map
def crop(image_path, coords):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    path = '{0}_{1}.png'.format(image_path,'_resize_sprite2')
    cropped_image.save(path)
    return path
def create_lb(i,j,block):
    label = QLabel()
    pic = QPixmap()
    if block == 3:
        pic = QPixmap('sprite.jpg__resize_sprite.png')
    elif block == 0 or block == 1:
        pic =  QPixmap('sprite.jpg__resize_sprite2.png')
    label.setPixmap(pic)
    grid.addWidget(label,i,j)
if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = QWidget()
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

    thread, thread2, thread3 = Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread()
    thread.output[int, int,int].connect(create_lb)
    thread2.output[int, int,int].connect(create_lb)
    thread3.output[int, int,int].connect(create_lb)
    thread.render(0, 0, h+1, 3,map_)
    thread2.render(0, 3, h+1, wh//2,map_)
    thread3.render(0, wh//2, h+1, wh + 1,map_)

    sys.exit(app.exec_())