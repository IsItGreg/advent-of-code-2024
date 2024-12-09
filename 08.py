import itertools

def part1():
    data = open('08.txt').read().strip().split('\n')

    data = [list(line) for line in data]

    antennaMap = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != '.':
                if data[y][x] not in antennaMap:
                    antennaMap[data[y][x]] = []
                antennaMap[data[y][x]].append((x, y))

    def isOnMap(node):
        return node[0] >= 0 and node[0] < len(data[0]) and node[1] >= 0 and node[1] < len(data)

    for antenna in antennaMap:
        pairs = itertools.combinations(antennaMap[antenna], 2)
        for pair in pairs:
            diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            node1 = (pair[1][0] + diff[0], pair[1][1] + diff[1])
            node2 = (pair[0][0] - diff[0], pair[0][1] - diff[1])
            if isOnMap(node1):
                data[node1[1]][node1[0]] = '#'
            if isOnMap(node2):
                data[node2[1]][node2[0]] = '#'


    print(sum(line.count('#') for line in data))    


def part2():
    data = open('08.txt').read().strip().split('\n')

    data = [list(line) for line in data]

    antennaMap = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != '.':
                if data[y][x] not in antennaMap:
                    antennaMap[data[y][x]] = []
                antennaMap[data[y][x]].append((x, y))

    def isOnMap(node):
        return node[0] >= 0 and node[0] < len(data[0]) and node[1] >= 0 and node[1] < len(data)

    for antenna in antennaMap:
        pairs = itertools.combinations(antennaMap[antenna], 2)
        for pair in pairs:
            diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            tempNode = (pair[1][0] + diff[0], pair[1][1] + diff[1])
            while isOnMap(tempNode):
                if data[tempNode[1]][tempNode[0]] == '.':
                    data[tempNode[1]][tempNode[0]] = '#'
                tempNode = (tempNode[0] + diff[0], tempNode[1] + diff[1])
            
            tempNode = (pair[1][0] - diff[0], pair[1][1] - diff[1])
            while isOnMap(tempNode):
                if data[tempNode[1]][tempNode[0]] == '.':
                    data[tempNode[1]][tempNode[0]] = '#'
                tempNode = (tempNode[0] - diff[0], tempNode[1] - diff[1])
            
            


    count = sum(line.count('.') for line in data)
    print(len(data) * len(data[0]) - count)
    

# part1()
part2()