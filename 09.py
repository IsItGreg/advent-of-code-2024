
def part1():
    data = open('09.txt').read().strip()
    print(data)

    nums = [int(x) for x in data]


    data = []
    count = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            data.extend([count] * num)
            count += 1
        else:
            data.extend([-1] * num)
            
    lptr = 0
    rptr = len(data) - 1

    while True:
        while data[lptr] != -1:
            lptr += 1
        while data[rptr] == -1:
            rptr -= 1
        if lptr >= rptr:
            break
        data[lptr], data[rptr] = data[rptr], data[lptr]

    checksum = 0
    for i, num in enumerate(data):
        if num == -1:
            break
        checksum += num * i

    print(checksum)

def part2():
    data = open('09.txt').read().strip()

    nums = [int(x) for x in data]

    count = 0
    pos = 0

    files = []
    spaces = []
    end = []
    for i, num in enumerate(nums):
        if i % 2 == 0:
            files.append((pos, num, count))
            for i in range(num):
                end.append(count)
            count += 1
        else:
            spaces.append((pos, num))
            for i in range(num):
                end.append(None)
        pos += num

    for file in reversed(files):
        for i, space in enumerate(spaces):
            if space[0] < file[0] and space[1] >= file[1]:
                for j in range(file[1]):
                    end[file[0]+j] = None
                    end[space[0]+j] = file[2]
                spaces[i] = (space[0] + file[1], space[1] - file[1])
                break

    checksum = 0

    for i, num in enumerate(end):
        if num is not None:
            checksum += i * num

    print(checksum)

# part1() 
part2()