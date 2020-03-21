import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication,QLabel)
from PyQt5.QtGui import (QPixmap,QPicture)
from PIL import Image
import Game_Thread
def crop(image_path, coords):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    path = '{0}_{1}.png'.format(image_path,'_resize_sprite')
    cropped_image.save(path)
    return path
def create_lb(i,j):
    label = QLabel()
    pic = QPixmap('sprite.jpg__resize_sprite.png')
    label.setPixmap(pic)
    grid.addWidget(label,i,j)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Game')
    w.setStyleSheet(open("style.qss", "r").read())
    w.showFullScreen()
    frame_sz = [w.frameSize().height()//16,w.frameSize().width()//16]
    img = crop('./sprite.jpg', (105, 14, 121, 30))
    image = QPixmap(img)
    grid = QGridLayout()
    grid.setSpacing(0)
    grid.setContentsMargins(0, 0, 0, 0)
    w.setLayout(grid)
    thread, thread2, thread3 = Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread(), Game_Thread.Draw_map_thread()
    thread.output[int, int].connect(create_lb)
    thread2.output[int, int].connect(create_lb)
    thread3.output[int, int].connect(create_lb)
    thread.render(0, 0, frame_sz[0] + 1, 20)
    thread2.render(0, 20, frame_sz[0] + 1, 40)
    thread3.render(0, 30, frame_sz[0] + 1, frame_sz[1] + 1)
    lb = QLabel("Rendering")
    lb.move(frame_sz[0]//2,frame_sz[1]//2)
    #create_lb("hello")
    sys.exit(app.exec_())