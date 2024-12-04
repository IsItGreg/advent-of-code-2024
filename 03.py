import re

def part1():
    with open('03.txt', 'r') as file:
        data = file.read()

    print(data)

    muls = re.findall(r'mul\(\d+,\d+\)', data)

    sum = 0

    for mul in muls:
        nums = re.findall(r'\d+', mul)
        sum += int(nums[0]) * int(nums[1])
        
    print(sum)


def part2():
    with open('03.txt', 'r') as file:
        data = file.read()

    print(data)

    muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

    sum = 0
    enabled = True

    for mul in muls:
        if mul == "don't()":
            enabled = False 
        elif mul == "do()":
            enabled = True
        elif enabled:
            nums = re.findall(r'\d+', mul)
            sum += int(nums[0]) * int(nums[1])
        
    print(sum)



# part1()
part2()
