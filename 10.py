

def part1():
    data = open('10.txt').read().strip().split('\n')

    data = [list(map(int, line)) for line in data]

    # print(data)

    zeroes = {}

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                zeroes[(i, j)] = set()

    def traverse(y, x, step, ny, nx):
        if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]) or data[y][x] != step:
            return 0
        if data[y][x] == 9:
            zeroes[(ny, nx)].add((y, x))
            return 1
        return traverse(y+1, x, step+1, ny, nx) + traverse(y-1, x, step+1, ny, nx) + traverse(y, x+1, step+1, ny, nx) + traverse(y, x-1, step+1, ny, nx)
    
    count = 0
    count2 = 0
    for zero in zeroes:
        count2 += traverse(zero[0], zero[1], 0, zero[0], zero[1])
        count += len(zeroes[zero])

    print(count)
    print(count2)

part1()
# accidentally solved part 2 within part 1