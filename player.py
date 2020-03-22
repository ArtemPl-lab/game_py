
class player(object):
    def __init__(self,grid,map_,player_pos = [1,1]):
        super().__init__()
        self.grid = grid
        self.map_ = map_
        self.player_posX = player_pos[1]
        self.player_posY = player_pos[0]
    def go_left(self):
        self
