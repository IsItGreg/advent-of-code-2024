
def part1():
    with open('02.txt', 'r') as file:
        data = file.read()
        lines = data.split('\n')

        badRowsCount = 0

        for line in lines:
            numbers = line.split()
            numbers = [int(num) for num in numbers]

            isDecreasing = numbers[0] > numbers[1]

            for a, b in zip(numbers[:-1], numbers[1:]):
                if isDecreasing and a < b:
                    badRowsCount += 1
                    break
                elif not isDecreasing and a >= b:
                    badRowsCount += 1
                    break
                elif abs(a - b) < 1 or abs(a - b) > 3:
                    badRowsCount += 1
                    break

        print(len(lines) - badRowsCount)

def part2():
    with open('02.txt', 'r') as file:
        data = file.read()
        lines = data.split('\n')

        badRowsCount = 0

        for line in lines:
            numbers = line.split()
            numbers = [int(num) for num in numbers]

            def checkRow(nums):
                isDecreasing = nums[0] > nums[1]

                for a, b in zip(nums[:-1], nums[1:]):
                    if (isDecreasing and a < b) or (not isDecreasing and a >= b) or abs(a - b) < 1 or abs(a - b) > 3:
                        return False
                return True
            
            rowWorks = False

            for indexToSkip in range(len(numbers)):
                # brute force :(
                rowToCheck = numbers[:indexToSkip] + numbers[indexToSkip + 1:]
                if checkRow(rowToCheck):
                    rowWorks = True
                    break
            
            if not rowWorks:
                badRowsCount += 1

        print(len(lines) - badRowsCount)



# part1()
part2()