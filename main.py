import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication,QLabel)
from PyQt5.QtGui import (QPixmap,QPicture)
from PIL import Image
import drawing_map
import QThread
def crop(image_path, coords):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    path = '{0}_{1}.png'.format(image_path,'_resize_sprite')
    cropped_image.save(path)
    return path
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Game')
    w.setStyleSheet(open("style.qss", "r").read())
    grid = QGridLayout()
    w.setLayout(grid)
    w.showFullScreen()
    frame_sz = [w.frameSize().height()//16,w.frameSize().width()//16]
    img = crop('./sprite.jpg', (105, 14, 121, 30))
    image = QPixmap(img)
    drawing_map.draw_map(grid, image)
    sys.exit(app.exec_())