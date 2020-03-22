import random
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
    mass[1][1] = 3
    unvisitedCount = get_unvisted_cells(mass)
    stack = []
    stack2 = []
    i = 0
    while unvisitedCount > 0:
        neighbours = get_neighbours(mass,current)
        if(len(neighbours) != 0):
            ran = random.randint(0, len(neighbours)-1)
            stack.append(current)
            neighbourCell = neighbours[ran]
            mass = remove_wall(current,neighbourCell,mass)
            current = neighbourCell
            mass[current[1]][current[0]] = 3
            i = 0
        elif (len(stack)>0):
            stack.pop()
            current = stack[len(stack)-1]
        unvisitedCount = get_unvisted_cells(mass)

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
            if (mcellCurrent != 3) and (cellCurrent != 0):
                cells.append(cellCurrent)
    return cells
def get_unvisted_cells(mass):
    sum = 0
    for i in mass:
        sum += i.count(1)
    return sum
def remove_wall(first,second,mass):
    xdif = second[0] - first[0]
    ydif = second[1] - first[1]
    addx = xdif // abs(xdif) if (xdif !=0) else 0
    addy = ydif // abs(ydif) if (ydif != 0) else 0
    targetX = first[0] + addx
    targetY = first[1] + addy
    mass[targetY][targetX] = 3
    return mass
def get_unvisited_cell(mass):
    pas = []
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if mass[i][j] == 1:
                pas.append([j,i])
    return pas
if __name__=="__main__":
    m = generate_mass(100,100)
    for i in m:
        print(*i)
    generate_lab(m)
    for i in m:
        print(*i)