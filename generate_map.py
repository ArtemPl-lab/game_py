def generate_mass(h,w):
    map = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if (i%2!=0 and j%2 != 0) and (i<h-1 and j<w-1):
                map[i][j] = 1
            else:
                map[i][j] = 0
    return map
def generate_lab(mass):
    start = [1,1]
    current = start
    while unvisitedCount > 0:
        neighbours = get_neighbours(len(mass[0]),len(mass),mass,current)

def get_neighbours(mas,current_pos):
    width = len(mas[0])
    height = len(mas)
    cells = []
    x = current_pos[0]
    y = current_pos[1]
    distance = 2
    up = [x, y - distance]
    rt = [x + distance, y]
    dw = [x, y + distance]
    lt = [x - distance, y]
    d = [up,rt,dw,lt]
    for i in range(4):
        if (d[i][0] > 0) and (d[i][0] < width) and (d[i][1] > 0) and (d[i][1] < height):
            mcellCurrent = mas[d[i][1]][d[i][0]]
            cellCurrent = d[i]
            if (mcellCurrent != 3) and (cellCurrent):
                cells.append(cellCurrent)
    return cells
if __name__=="__main__":
    m = generate_mass(100,100)
    for i in m:
        print(*i)