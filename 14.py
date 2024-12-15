
import numpy as np


def part1():
    data = open('14.txt').read().strip()
    lines = data.split('\n')

    steps = 100
    dims = (101, 103)
    # dims = (11, 7)

    ps = []
    vs = []
    for line in lines:
        p, v = line.split(' ')
        px, py = p.split('=')[1].split(',')
        vx, vy = v.split('=')[1].split(',')
        ps.append((int(px), int(py)))
        vs.append((int(vx), int(vy)))

    fps = []
    for p, v in zip(ps, vs):
        move = (v[0] * steps, v[1] * steps)
        np = ((p[0] + move[0]) % dims[0], (p[1] + move[1]) % dims[1])
        # if (np[0] == dims[0] // 2) or (np[1] == dims[1] // 2):
        #     continue
        fps.append(np)

    tl, tr, bl, br = 0, 0, 0, 0
    for p in fps:
        if p[0] > dims[0] // 2:
            if p[1] > dims[1] // 2:
                br += 1
            if p[1] < dims[1] // 2:
                tr += 1
        if p[0] < dims[0] // 2:
            if p[1] > dims[1] // 2:
                bl += 1
            if p[1] < dims[1] // 2:
                tl += 1

    print(tl, tr, bl, br)
    print(tl * tr * bl * br)

def part2():
    data = open('14.txt').read().strip()
    lines = data.split('\n')

    dims = (101, 103)
    # dims = (11, 7)
    mx = dims[0] // 2

    ps = []
    vs = []
    for line in lines:
        p, v = line.split(' ')
        px, py = p.split('=')[1].split(',')
        vx, vy = v.split('=')[1].split(',')
        ps.append((int(px), int(py)))
        vs.append((int(vx), int(vy)))

    def printTable(ps):
        table = [['.' for _ in range(dims[0])] for _ in range(dims[1])]
        for p in ps:
            table[p[1]][p[0]] = '#'
        for row in table:
            print(''.join(row))

    def step(ps):
        nps = []
        for p, v in zip(ps, vs):
            np = ((p[0] + v[0]) % dims[0], (p[1] + v[1]) % dims[1])
            nps.append(np)
        return nps
    

    
    def getNeighbors(i, j):
        neighbors = set()
        if i > 0:
            neighbors.add((i - 1, j))
        if i < dims[0] - 1:
            neighbors.add((i + 1, j))
        if j > 0:
            neighbors.add((i, j - 1))
        if j < dims[1] - 1:
            neighbors.add((i, j + 1))
        return neighbors
    

    stepcount = 0
    while True:
        ps = step(ps)
        stepcount += 1

        grid = [['.' for _ in range(dims[0])] for _ in range(dims[1])]
        for p in ps:
            grid[p[1]][p[0]] = '#'
        
        seen = set()
        distinct = 0
        for x in range(dims[0]):
            for y in range(dims[1]):
                if (x, y) not in seen and grid[y][x] == '#':
                    distinct += 1
                    seen.add((x, y))
                    locsToCheck = getNeighbors(x, y)
                    while len(locsToCheck) > 0:
                        loc = locsToCheck.pop()
                        if loc not in seen:
                            seen.add(loc)
                            if grid[loc[1]][loc[0]] == '#':
                                locsToCheck.update(getNeighbors(loc[0], loc[1]))
        if distinct < 300:
            break

        

    printTable(ps)
    print(stepcount)


# part1()
part2()
