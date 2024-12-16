def printGrid(grid):
    for row in grid:
        print(''.join(row))

def part1():
    data = open('15.txt').read().strip()
    grid, steps = data.split('\n\n')

    grid = grid.split('\n')
    grid = [list(row) for row in grid]

    steps = list(steps.replace('\n', ''))

    dirmap = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    robotPos = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                robotPos = (j, i)
                break

    print(grid, steps, robotPos)

    for step in steps:
        dir = dirmap[step]
        opening = robotPos
        while grid[opening[1]][opening[0]] != '.':
            opening = (opening[0] + dir[0], opening[1] + dir[1])
            if grid[opening[1]][opening[0]] == '#':
                opening = None
                break

        if opening is None:
            continue
        
        grid[robotPos[1]][robotPos[0]] = '.'
        temp = opening
        
        while temp != robotPos:
            next = (temp[0] - dir[0], temp[1] - dir[1])
            grid[temp[1]][temp[0]] = grid[next[1]][next[0]]
            temp = next

        robotPos = (robotPos[0] + dir[0], robotPos[1] + dir[1])
        grid[robotPos[1]][robotPos[0]] = '@'

    printGrid(grid)    

    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                score += x + (y * 100)

    print(score)


def part2():
    data = open('15.txt').read().strip()
    grid, steps = data.split('\n\n')

    grid = grid.split('\n')
    grid = [list(row) for row in grid]

    steps = list(steps.replace('\n', ''))

    dirmap = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    ngrid = []
    for y in range(len(grid)):
        ngrid.append([])
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                ngrid[y].extend(['#', '#'])
            elif grid[y][x] == '@':
                ngrid[y].extend(['@', '.'])
            elif grid[y][x] == 'O':
                ngrid[y].extend(['[', ']'])
            else:
                ngrid[y].extend(['.', '.'])

    grid = ngrid

    printGrid(grid)

    robotPos = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                robotPos = (j, i)
                break

    for step in steps:
        dir = dirmap[step]
        
        thingsToMove = []
        thingsChecked = []
        thingsToCheck = [robotPos]
        blocked = False

        while len(thingsToCheck) > 0:
            thing = thingsToCheck.pop(0)
            if thing in thingsChecked:
                continue
            thingsChecked.append(thing)

            if grid[thing[1]][thing[0]] == '@':
                thingsToCheck.append((thing[0] + dir[0], thing[1] + dir[1]))
                thingsToMove.append((thing[0], thing[1]))
            elif grid[thing[1]][thing[0]] == '[':
                thingsToCheck.append((thing[0] + dir[0], thing[1] + dir[1]))
                thingsToMove.append((thing[0], thing[1]))
                thingsToCheck.append((thing[0] + 1, thing[1]))
            elif grid[thing[1]][thing[0]] == ']':
                thingsToCheck.append((thing[0] + dir[0], thing[1] + dir[1]))
                thingsToMove.append((thing[0], thing[1]))
                thingsToCheck.append((thing[0] - 1, thing[1]))
            elif grid[thing[1]][thing[0]] == '#':
                blocked = True
                break

            # print(thing, grid[thing[1]][thing[0]], thingsToCheck, thingsChecked, thingsToMove)

        if blocked:
            continue

        for thing in reversed(thingsToMove):
            item = grid[thing[1]][thing[0]]
            if item == '@':
                robotPos = (thing[0] + dir[0], thing[1] + dir[1])
            grid[thing[1]][thing[0]] = grid[thing[1] + dir[1]][thing[0] + dir[0]]
            grid[thing[1] + dir[1]][thing[0] + dir[0]] = item

        
        # printGrid(grid)    

    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '[':
                score += x + (y * 100)

    print(score)

# part1()
part2()