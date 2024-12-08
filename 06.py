
def part1():
    with open('06.txt', 'r') as file:
        data = file.read()

    rows = data.split('\n')
    rows = [list(row) for row in rows]

    guardPos = None
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == '^':
                guardPos = (i, j)
                break
        if guardPos is not None:
            break

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    while True:
        nextPos = (guardPos[0] + directions[direction][0], guardPos[1] + directions[direction][1])
        if nextPos[0] < 0 or nextPos[0] >= len(rows) or nextPos[1] < 0 or nextPos[1] >= len(rows[nextPos[0]]):
            break
        if rows[nextPos[0]][nextPos[1]] == '#':
            direction = (direction + 1) % 4
            continue
        guardPos = nextPos
        rows[guardPos[0]][guardPos[1]] = '^'

    for row in rows:
        print(''.join(row))

    wholeMap = ''.join([''.join(row) for row in rows])
    print(wholeMap.count('^'))

    return rows


def part2():
    with open('06.txt', 'r') as file:
        data = file.read()

    rows = data.split('\n')
    rows = [list(row) for row in rows]

    guardPos = None
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == '^':
                guardPos = (i, j)
                break
        if guardPos is not None:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    count = 0

    part1Rows = part1()

    for i in range(len(rows)):
        print(i)
        for j in range(len(rows[i])):
            tGuardPos = tuple(guardPos)
            tDirection = direction
            if part1Rows[i][j] != '^' or rows[i][j] != '.':
                continue
            hasLoop = False
            rows[i][j] = '#'
            history = []
            while True:
                nextPos = (tGuardPos[0] + directions[tDirection][0], tGuardPos[1] + directions[tDirection][1])
                if nextPos[0] < 0 or nextPos[0] >= len(rows) or nextPos[1] < 0 or nextPos[1] >= len(rows[nextPos[0]]):
                    break
                if rows[nextPos[0]][nextPos[1]] == '#':
                    tDirection = (tDirection + 1) % 4
                    continue
                tGuardPos = nextPos
                if (tGuardPos, tDirection) in history:
                    hasLoop = True
                    break
                history.append((tGuardPos, tDirection))   

            rows[i][j] = '.'
            if hasLoop:
                count += 1
            
    print(count)
# part1()
part2()
