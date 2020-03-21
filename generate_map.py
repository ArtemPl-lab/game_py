def generate_mass(h,w):
    map = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if (i%2!=0 and j%2 != 0) and (i<h-1 and j<w-1):
                map[i][j] = 1
            else:
                map[i][j] = 0
    return map
if __name__=="__main__":
    m = generate_mass(100,100)
    for i in m:
        print(*i)