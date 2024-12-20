
def part1():
    data = open('19.txt').read().strip()

    towels, patterns = data.split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.split('\n')

    towels = set(towels)

    knownPossible = set()
    knownImpossible = set()

    def canMake(pattern):
        if pattern in towels or pattern in knownPossible:
            return True
        
        if pattern in knownImpossible:
            return False

        for i in range(1, len(pattern)):
            if pattern[:i] in towels and canMake(pattern[i:]):
                knownPossible.add(pattern)
                return True
        
        knownImpossible.add(pattern)
        return False

    count = 0
    for pattern in patterns:
        print(pattern)
        if canMake(pattern):
            count += 1
    print(count)


def part2():
    data = open('19.txt').read().strip()

    towels, patterns = data.split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.split('\n')

    towels = set(towels)

    knownWays = {}

    def canMake(pattern):
        if len(pattern) == 0:
            return 1
        if len(pattern) == 1:
            return 1 if pattern in towels else 0
        
        if pattern in knownWays:
            return knownWays[pattern]

        ways = 0
        for i in range(1, len(pattern)+1):
            if pattern[:i] in towels:
                ways += canMake(pattern[i:])
                
        knownWays[pattern] = ways
        return ways

    count = 0
    for pattern in patterns:
        print(pattern, canMake(pattern))
        count += canMake(pattern)
    print(count)

    # print(canMake('gbbr'))


# part1()
part2()