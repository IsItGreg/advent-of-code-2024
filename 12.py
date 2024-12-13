
def part1():
    data = open('12.txt').read().strip()
    data = data.split('\n')
    data = [list(line) for line in data]

    def getNeighbors(i, j):
        neighbors = set()
        if i > 0:
            neighbors.add((i - 1, j))
        if i < len(data) - 1:
            neighbors.add((i + 1, j))
        if j > 0:
            neighbors.add((i, j - 1))
        if j < len(data[0]) - 1:
            neighbors.add((i, j + 1))
        return neighbors

    map = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char in map:
                map[char].add((i, j))
            else:
                map[char] = set([(i, j)])

    newMap = {}
    for char in map:
        i = 0
        while len(map[char]) > 0:
            newChar = char + str(i)
            loc = map[char].pop()
            newMap[newChar] = set([loc])

            visited = set()
            locsToCheck = getNeighbors(loc[0], loc[1])
            while len(locsToCheck) > 0:
                x, y = locsToCheck.pop()
                if (x, y) in map[char] and (x, y) not in visited:
                    locsToCheck.update(getNeighbors(x, y))
                    newMap[newChar].add((x, y))
                    map[char].remove((x, y))
                visited.add((x, y))

            i += 1
            
    map = newMap

    perimeterMap = {}
    for char in map:
        for i, j in map[char]:
            fences = 4
            for x, y in getNeighbors(i, j):
                if (x, y) in map[char]:
                    fences -= 1
            if char in perimeterMap:
                perimeterMap[char] += fences
            else:
                perimeterMap[char] = fences

    sum = 0
    for char in perimeterMap:
        sum += perimeterMap[char] * len(map[char])
    print(sum)


def part2():
    data = open('12.txt').read().strip()
    data = data.split('\n')
    data = [list(line) for line in data]

    def getNeighbors(i, j):
        neighbors = set()
        if i > 0:
            neighbors.add((i - 1, j))
        if i < len(data) - 1:
            neighbors.add((i + 1, j))
        if j > 0:
            neighbors.add((i, j - 1))
        if j < len(data[0]) - 1:
            neighbors.add((i, j + 1))
        return neighbors

    map = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char in map:
                map[char].add((i, j))
            else:
                map[char] = set([(i, j)])

    newMap = {}
    for char in map:
        i = 0
        while len(map[char]) > 0:
            newChar = char + str(i)
            loc = map[char].pop()
            newMap[newChar] = set([loc])

            visited = set()
            locsToCheck = getNeighbors(loc[0], loc[1])
            while len(locsToCheck) > 0:
                x, y = locsToCheck.pop()
                if (x, y) in map[char] and (x, y) not in visited:
                    locsToCheck.update(getNeighbors(x, y))
                    newMap[newChar].add((x, y))
                    map[char].remove((x, y))
                visited.add((x, y))

            i += 1
            
    map = newMap

    def getPerimeter(shape):
        corners = set()
        weirdDiag = 0
        for i, j in shape:
            tcorners = set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
            corners = corners.symmetric_difference(tcorners)
            if (i + 1, j + 1) in shape and (i + 1, j) not in shape and (i, j + 1) not in shape:
                weirdDiag += 2
            if (i - 1, j + 1) in shape and (i - 1, j) not in shape and (i, j + 1) not in shape:
                weirdDiag += 2
        return len(corners) + weirdDiag


    # print(getPerimeter(map['A0']))

    sum = 0
    for char in map:
        # print(char, getPerimeter(map[char]), len(map[char]))
        sum += getPerimeter(map[char]) * len(map[char])
    print(sum)
    

# part1()
part2()
