
def part1():
    with open('01.txt', 'r') as file:
        data = file.read()
        lines = data.split('\n')

        left = []
        right = []

        for line in lines[:-1]:
            leftStr, rightStr = line.split()

            leftNum = int(leftStr)
            rightNum = int(rightStr)

            left.append(leftNum)
            right.append(rightNum)

        left.sort()
        right.sort()

        diff = 0

        for i in range(len(left)):
            diff += abs(left[i] - right[i])

        print(diff)

def part2():
    with open('01.txt', 'r') as file:
        data = file.read()
        lines = data.split('\n')

        left = []
        right = []

        for line in lines:
            leftStr, rightStr = line.split()

            leftNum = int(leftStr)
            rightNum = int(rightStr)

            left.append(leftNum)
            right.append(rightNum)
        
        rightCountMap = {}

        for rightNum in right:
            rightCountMap[rightNum] = rightCountMap.get(rightNum, 0) + 1

        print(rightCountMap)

        score = 0
        for leftNum in left:
            score += rightCountMap.get(leftNum, 0) * leftNum

        print(score)

# part1()
part2()