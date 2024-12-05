
def part1():
    with open('04.txt', 'r') as file:
        data = file.read()

    lines = data.split('\n')

    stringToFind = 'XMAS'

    directions = [
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    ]

    def isValid(x, y):
        return x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)
    
    def checkDir(x, y, dir):
        endX = x + dir[0] * (len(stringToFind) - 1)
        endY = y + dir[1] * (len(stringToFind) - 1)
    
        if isValid(endX, endY):
            for i in range(len(stringToFind)):
                if lines[y + dir[1] * i][x + dir[0] * i] != stringToFind[i]:
                    return False
            return True
        return False


    count = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'X':
                for dir in directions:
                    if checkDir(x, y, dir):
                        # print(x, y, dir)
                        count += 1

    print(count)


def part2():
    with open('04.txt', 'r') as file:
        data = file.read()

    lines = data.split('\n')

    diagDirs = [
        (1, -1),
        (1, 1),
        (-1, -1),
        (-1, 1)
    ]

    count = 0

    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[y]) - 1):
            if lines[y][x] == 'A':
                tL = lines[y-1][x-1]
                bR = lines[y+1][x+1]
                tR = lines[y-1][x+1]
                bL = lines[y+1][x-1]

                if tL + bR in ['MS', 'SM'] and tR + bL in ['MS', 'SM']:
                    count += 1

                
    print(count)




# part1()
part2()