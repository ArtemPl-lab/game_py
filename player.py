from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class player:
    def __init__(self, grid, map_, image_):
        super().__init__()
        self.grid = grid
        self.map_ = map_
        self.player_posX = 1
        self.player_posY = 1
        self.image = image_
        self.player_stack = []
    def go_left(self):
        if (self.player_posX-1 > 0) and (self.player_posX-1 < len(self.map_[0])) and (self.player_posY > 0) and (self.player_posY < len(self.map_)):
            if self.map_[self.player_posY][self.player_posX-1] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posX -= 1
                self.update()
    def go_right(self):
        if (self.player_posX+1 > 0) and (self.player_posX+1 < len(self.map_[0])) and (self.player_posY > 0) and (self.player_posY < len(self.map_)):
            if self.map_[self.player_posY][self.player_posX+1] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posX += 1
                self.update()
    def go_up(self):
        if (self.player_posX > 0) and (self.player_posX < len(self.map_[0])) and (self.player_posY-1 > 0) and (self.player_posY-1 < len(self.map_)):
            if self.map_[self.player_posY-1][self.player_posX] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posY -= 1
                self.update()
    def go_down(self):
        if (self.player_posX > 0) and (self.player_posX < len(self.map_[0])) and (self.player_posY+1 > 0) and (self.player_posY+1 < len(self.map_)):
            if self.map_[self.player_posY+1][self.player_posX] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posY += 1
                self.update()
    def update(self):
        if (self.player_posX > 0) and (self.player_posX < len(self.map_[0])) and (self.player_posY > 0) and (self.player_posY < len(self.map_)):
            lb = QLabel()
            lb.setPixmap(self.image)
            self.grid.addWidget(lb, self.player_posY, self.player_posX)
            if len(self.player_stack) != 0:
                st_pos = self.player_stack[len(self.player_stack) - 1]
                lb2 = QLabel()
                pic = QPixmap('sprite.jpg__resize_sprite.png')
                lb2.setPixmap(pic)
                self.grid.addWidget(lb2, st_pos[1], st_pos[0])
    def draw_line(self,fl):
        if fl:
            pic = QPixmap('line.png')
        else:
            pic = QPixmap('sprite.jpg__resize_sprite.png')
        for i in self.player_stack:
            lab = QLabel()
            lab.setPixmap(pic)
            self.grid.addWidget(lab,i[1],i[0])