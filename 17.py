

def part1():
    data = open('17.txt').read().strip()
    registers, program = data.split('\n\n')
    registers = registers.split('\n')
    registers = [int(register.split(': ')[1]) for register in registers]
    program = program.split(': ')[1]
    program = [int(instruction) for instruction in program.split(',')]

    print(registers)
    print(program)

    a, b, c = registers

    def getOpVal(op):
        if op in [0, 1, 2, 3]: return op
        if op == 4: return a
        if op == 5: return b
        if op == 6: return c
        if op == 7: raise Exception('Unknown operand')

    outputs = []

    # a,b,c = 117440,0,0
    a = 164542125272765
    # program = [0,1,5,4,3,0]

    i = 0
    while i < len(program):
        inst = program[i]
        op = program[i + 1]
        print(inst, op)
        if inst == 0:
            a = (a // (2 ** getOpVal(op)))
        elif inst == 1:
            b = b ^ op
        elif inst == 2:
            b = getOpVal(op) % 8
        elif inst == 3:
            if a != 0:
                i = op
                continue
        elif inst == 4:
            b = b ^ c
        elif inst == 5:
            outputs.append(str(getOpVal(op) % 8))
        elif inst == 6:
            b = (a // (2 ** getOpVal(op)))
        elif inst == 7:
            c = (a // (2 ** getOpVal(op)))
        i += 2

    print(a, b, c)

    print(','.join(outputs))



def part2():
    def step(a):
        b = a % 8
        b = b ^ 1
        c = a // (2 ** b)
        b = b ^ 5
        a = a // 8
        b = b ^ c
        b = b % 8

        return (a, b)
    
    numsToTry = [0, 1, 2, 3, 4, 5, 6, 7]

    target = [2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0]

    t = len(target) - 1

    while t >= 0:
        nextNumsToTry = []
        for num in numsToTry:
            a,b = step(num)
            # print(target[len(target) - i - 1], b)
            if b == target[t]:
                print ('this one: ', num, a,b)
                nextNumsToTry.extend(range(num * 8, num * 8 + 8))
            # print(num, a,b)
            
        numsToTry = nextNumsToTry
        t -= 1




part1()
# part2()
