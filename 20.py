
def part1():
    data = open('20.txt').read().strip()

    data = data.split('\n')
    data = [list(row) for row in data]

    for row in data:
        print(''.join(row))

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                start = (x, y)
            elif data[y][x] == 'E':
                end = (x, y)

    print(start, end)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    step = end
    t = 0

    distFromEnd = {}
    skippableWalls = {}

    while True:
        visited.add(step)
        distFromEnd[step] = t
        
        pstep = step
        for dir in dirs:
            nextStep = (pstep[0] + dir[0], pstep[1] + dir[1])

            if data[nextStep[1]][nextStep[0]] == '#':
                if nextStep not in skippableWalls:
                    skippableWalls[nextStep] = set()
                skippableWalls[nextStep].add(pstep)
                continue
            if data[nextStep[1]][nextStep[0]] != '#' and nextStep not in visited:
                step = nextStep
        if pstep == start:
            break
        t += 1
            
            
    print(t)
    skippableWalls = {k: v for k, v in skippableWalls.items() if len(v) > 1}

    print(len(skippableWalls))

    shortcuts = {}
    for k, v in skippableWalls.items():
        # print(k, v)
        dists = [distFromEnd[w] for w in v]
        dists.sort()
        # print(dists)
        closest = dists[0]
        for dist in dists[1:]:
            if dist - closest - 2 not in shortcuts:
                shortcuts[dist - closest - 2] = 0
            shortcuts[dist - closest - 2] += 1

    print(shortcuts)

    shortcuts = sorted(shortcuts.items(), key=lambda x: x[0])
    print(shortcuts)

    count = 0
    for saved, number in shortcuts:
        if saved >= 100:
            count += number

    print(count)

def part2():
    data = open('20.txt').read().strip()

    data = data.split('\n')
    data = [list(row) for row in data]

    for row in data:
        print(''.join(row))

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                start = (x, y)
            elif data[y][x] == 'E':
                end = (x, y)

    print(start, end)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    quads = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    step = end
    t = 0

    visited = set()
    distFromEnd = {}
    
    shortcuts = set()
    
    while True:
        for dy in range(21):
            for dx in range(21):
                if dx + dy > 20:
                    continue
                for quad in quads:
                    target = (step[0] + dx * quad[0], step[1] + dy * quad[1])
                    if target in visited:
                        shortcuts.add((step, target, dx + dy))
                

        visited.add(step)
        distFromEnd[step] = t

        pstep = step
        for dir in dirs:
            nextStep = (pstep[0] + dir[0], pstep[1] + dir[1])
            if data[nextStep[1]][nextStep[0]] != '#' and nextStep not in visited:
                step = nextStep
        if pstep == start:
            break
        t += 1
            
            
    dsd = {}
    for sc in shortcuts:
        distSaved = distFromEnd[sc[0]] - distFromEnd[sc[1]] - sc[2]
        if distSaved not in dsd:
            dsd[distSaved] = 0
        dsd[distSaved] += 1

    shortcuts = sorted(dsd.items(), key=lambda x: x[0])
    # print(shortcuts)

    count = 0
    for saved, number in shortcuts:
        if saved >= 100:
            count += number

    print(count)

# part1()
part2()