

def part1():
    data = open('16.txt').read().strip()
    grid = data.split('\n')
    grid = [list(row) for row in grid]

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    scores = {}
    locsToCheck = [(1, len(grid) - 2, 1, 0)]
    

    while len(locsToCheck) > 0:
        x, y, dir, score = locsToCheck.pop(0)

        if (x, y, dir) in scores and score >= scores[(x, y, dir)]:
            continue

        scores[(x, y, dir)] = score

        for i in range(len(dirs)):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            if grid[ny][nx] != '#':
                locsToCheck.append((nx, ny, i, score + (1 if i == dir else 1001)))

    print(scores)
    print(min([scores[(len(grid[1]) - 2, 1, i)] for i in range(len(dirs)) if (len(grid[1]) - 2, 1, i) in scores]))


def part2():
    data = open('16.txt').read().strip()
    grid = data.split('\n')
    grid = [list(row) for row in grid]

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    scores = {}
    locsToCheck = [(1, len(grid) - 2, 1, 0, None)]

    lastSquares = {None: set()}
    

    while len(locsToCheck) > 0:
        x, y, dir, score, lastSquare = locsToCheck.pop(0)
        currentSquare = (x, y, dir)

        if currentSquare in scores and score == scores[currentSquare]:
            lastSquares[currentSquare].add(lastSquare)
            print(lastSquares[currentSquare], currentSquare, lastSquare)

        if currentSquare in scores and score >= scores[currentSquare]:
            continue

        lastSquares[currentSquare] = set([lastSquare])

        scores[currentSquare] = score

        for i in [0, 1, 3]:
            ndir = (dir + i) % len(dirs)
            nx, ny = x + dirs[ndir][0], y + dirs[ndir][1]
            if grid[ny][nx] != '#':
                locsToCheck.append((nx, ny, ndir, score + (1 if i == 0 else 1001), currentSquare))

    # print(scores)
    minScore = min([scores[(len(grid[1]) - 2, 1, i)] for i in range(len(dirs)) if (len(grid[1]) - 2, 1, i) in scores])
    print(minScore)

    backTrace = set([(len(grid[1]) - 2, 1, i) for i in range(len(dirs)) if (len(grid[1]) - 2, 1, i) in scores and scores[(len(grid[1]) - 2, 1, i)] == minScore])

    paths = set()

    # print(lastSquares)

    print(backTrace)

    while len(backTrace) > 0:
        step = backTrace.pop()
        # print(step, lastSquares[step])
        if step != None:
            paths.add((step[0], step[1]))
        backTrace = backTrace.union(lastSquares[step])
        

    print(len(paths))

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if (j, i) in paths:
    #             print('O', end='')
    #         else:
    #             print(grid[i][j], end='')
    #     print()




# part1()
part2()