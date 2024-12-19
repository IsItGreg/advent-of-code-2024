

def part1():
    data = open('18.txt').read().strip().split('\n')
    gx = gy = 71
    steps = 1024

    grid = [['.' for _ in range(gx)] for _ in range(gy)]
    data = [(int(x), int(y)) for x,y in [line.split(',') for line in data]]

    for x,y in data[0:steps]:
        grid[y][x] = '#'

    for line in grid:
        print(''.join(line))

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = (0, 0)
    end = (gx-1, gy-1)

    wave = set([start])
    dist = 0
    checked = set()
    while True:
        nwave = set()
        print(len(wave))
        for x,y in wave:
            if (x,y) == end:
                print(dist)
                for line in grid:
                    print(''.join(line))
                return

            checked.add((x,y))
            grid[y][x] = 'O'

            for dx,dy in dirs:
                nx,ny = x + dx, y + dy
                if 0 <= nx < gx and 0 <= ny < gy and (nx, ny) not in checked:
                    if grid[ny][nx] != '#':
                        nwave.add((nx, ny))
        wave = nwave
        dist += 1

        # for line in grid:
        #     print(''.join(line))
        # print(dist)



def part2():
    data = open('18.txt').read().strip().split('\n')
    gx = gy = 71
    steps = 1024

    grid = [['.' for _ in range(gx)] for _ in range(gy)]
    data = [(int(x), int(y)) for x,y in [line.split(',') for line in data]]

    for x,y in data[0:steps]:
        grid[y][x] = '#'

    for line in grid:
        print(''.join(line))

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = (0, 0)
    end = (gx-1, gy-1)

    def getPath():
        last = {}

        wave = set([start])
        dist = 0
        checked = set()
        while len(wave) > 0:
            nwave = set()
            # print(len(wave))
            for x,y in wave:
                if (x,y) == end:
                    print(dist)
                    # for line in grid:
                    #     print(''.join(line))

                    path = set()
                    while (x,y) != start:
                        path.add((x,y))
                        x,y = last[(x,y)]
                    path.add(start)
                    return path

                checked.add((x,y))
                # grid[y][x] = 'O'

                for dx,dy in dirs:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < gx and 0 <= ny < gy and (nx, ny) not in checked:
                        if grid[ny][nx] != '#':
                            last[(nx, ny)] = (x, y)
                            nwave.add((nx, ny))
            wave = nwave
            dist += 1
        return None

    path = getPath()

    for x,y in data[steps:]:
        grid[y][x] = '#'
        for line in grid:
            print(''.join(line))
        print(x,y)
        if (x,y) in path:
            path = getPath()
            if path is None:
                print(x,y)
                return
        


# part1()
part2()
