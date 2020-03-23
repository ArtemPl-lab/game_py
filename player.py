from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class player:
    def __init__(self, grid, map_,pl_pos, finish_pos, image_):
        super().__init__()
        self.grid = grid
        self.map_ = map_
        self.player_posX = pl_pos[0]
        self.player_posY = pl_pos[1]
        self.image = image_
        self.player_stack = []
        self.finish_pos = finish_pos
    def go_left(self):
        if (self.player_posX-1 > 0) and (self.player_posX-1 < len(self.map_[0])) and (self.player_posY > 0) and (self.player_posY < len(self.map_)):
            if self.map_[self.player_posY][self.player_posX-1] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posX -= 1
                self.update()
                return True
            else:
                return False
        else:
            return False
    def go_right(self):
        if (self.player_posX+1 > 0) and (self.player_posX+1 < len(self.map_[0])) and (self.player_posY > 0) and (self.player_posY < len(self.map_)):
            if self.map_[self.player_posY][self.player_posX+1] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posX += 1
                self.update()
                return True
            else:
                return False
        else:
            return False
    def go_up(self):
        if (self.player_posX > 0) and (self.player_posX < len(self.map_[0])) and (self.player_posY-1 > 0) and (self.player_posY-1 < len(self.map_)):
            if self.map_[self.player_posY-1][self.player_posX] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posY -= 1
                self.update()
                return True
            else:
                return False
        else:
            return False
    def go_down(self):
        if (self.player_posX > 0) and (self.player_posX < len(self.map_[0])) and (self.player_posY+1 > 0) and (self.player_posY+1 < len(self.map_)):
            if self.map_[self.player_posY+1][self.player_posX] != 0:
                self.player_stack.append([self.player_posX, self.player_posY])
                self.player_posY += 1
                self.update()
                return True
            else:
                return False
        else:
            return False
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
        if self.player_posX == self.finish_pos[0] and self.player_posY == self.finish_pos[1]:
            print("finished!")
        finish_pic = QPixmap('finish.png')
        flb = QLabel()
        flb.setPixmap(finish_pic)
        self.grid.addWidget(flb,self.finish_pos[1],self.finish_pos[0])

    def draw_line(self,fl):
        if fl:
            pic = QPixmap('line.png')
        else:
            pic = QPixmap('sprite.jpg__resize_sprite.png')
        for i in self.player_stack:
            lab = QLabel()
            lab.setPixmap(pic)
            self.grid.addWidget(lab,i[1],i[0])
    def teleported(self,x,y):
        if (x > 0) and (x < len(self.map_[0])) and (y > 0) and (y < len(self.map_)):
            self.player_stack.append([self.player_posX, self.player_posY])
            self.player_posX = x
            self.player_posY = y
            self.update()
    def isTeleported(self,tp):
        for i in tp:
            if self.player_posX == i[0][0] and self.player_posY == i[0][1]:
                self.teleported(i[1][0], i[1][0])
                tp.remove(i)