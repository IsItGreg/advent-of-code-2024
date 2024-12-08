
def part1():
    data = open('07.txt').read().strip().split('\n')

    sum = 0
    for line in data:
        [target, nums] = line.split(': ')
        target = int(target)
        nums = list(map(int, nums.split(' ')))


        def recurse(nums, target, tsum, depth):
            if len(nums) == 0:
                return tsum == target

            return recurse(nums[1:], target, tsum + nums[0], depth + 1) or recurse(nums[1:], target, tsum * nums[0], depth + 1)

        if recurse(nums, target, 0, 0):
            sum += target

    print(sum)

def part2():
    data = open('07.txt').read().strip().split('\n')

    sum = 0
    for line in data:
        [target, nums] = line.split(': ')
        target = int(target)
        nums = list(map(int, nums.split(' ')))


        def recurse(nums, target, tsum, depth):
            if len(nums) == 0:
                return tsum == target

            return recurse(nums[1:], target, tsum + nums[0], depth + 1) or recurse(nums[1:], target, tsum * nums[0], depth + 1) or recurse(nums[1:], target, int(str(tsum) + str(nums[0])), depth + 1)

        if recurse(nums, target, 0, 0):
            sum += target

    print(sum)

# part1()
part2()