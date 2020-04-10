from PyQt5.QtCore import *
import time
class Draw_map_thread(QThread):
    output = pyqtSignal(int,int,int)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
    def __del__(self):
        self.exiting = True
        self.wait()
    def render(self,start1,start2,end1,end2,map):
        self.startI = start1
        self.startJ = start2
        self.endI = end1
        self.endJ = end2
        self.map = map
        self.start()
    def run(self):
        for i in range(self.startI,self.endI):
            for j in range(self.startJ,self.endJ):
                if i<len(self.map) and j<len(self.map[i]):
                    self.output.emit(i,j,self.map[i][j])
                else:
                    self.output.emit(i,j,0)
                time.sleep(0.01)