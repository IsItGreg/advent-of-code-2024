
def part1():
    data = open('11x.txt').read().strip()

    stones = data.split(' ')
    stones = [int(x) for x in stones]

    stones = [4048, 4048, 8096]
    blinks = 7

    stones = [0]
    blinks = 11

    # blinks = 25
    testcount = 0
    for _ in range(blinks):
        i = 0
        while i < len(stones):
            stone = stones.pop(i)
            if stone == 0:
                stones.insert(i, 1)
                testcount += 1
            elif len(str(stone)) % 2 == 0:
                stonestr = str(stone)
                midpoint = len(stonestr) // 2
                stones.insert(i, int(stonestr[:midpoint]))
                stones.insert(i+1, int(stonestr[midpoint:]))
                i += 1
            else:
                newstone = int(stone) * 2024
                stones.insert(i, newstone)
            i += 1
    print(testcount)
    print(len(stones))


def part2():

    data = open('11.txt').read().strip()

    stones = data.split(' ')
    stones = [int(x) for x in stones]

    blinks = 75

    map = {}
    def blink(stone, stepsLeft):
        if stepsLeft == 0:
            return 1
        if (stone, stepsLeft) in map:
            return map[(stone, stepsLeft)]
        if stone == 0:
            value = blink(1, stepsLeft - 1)
        elif len(str(stone)) % 2 == 0:
            value = blink(int(str(stone)[:len(str(stone))//2]), stepsLeft - 1) + blink(int(str(stone)[len(str(stone))//2:]), stepsLeft - 1)
        else:
            value = blink(stone * 2024, stepsLeft - 1)
        map[(stone, stepsLeft)] = value
        return value
    
    total = 0
    for stone in stones:
        total += blink(stone, blinks)
    print(total)


# part1()
part2()

