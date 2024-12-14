import math
from z3 import *
def part1():
    data = open('13.txt').read().strip()

    total = 0
    sections = data.split('\n\n')
    for section in sections:
        lines = section.split('\n')
        a = lines[0].split(' ')
        ax = int(a[2][:-1].split('+')[1])
        ay = int(a[3].split('+')[1])
        b = lines[1].split(' ')
        bx = int(b[2][:-1].split('+')[1])
        by = int(b[3].split('+')[1])
        px = int(lines[2].split(' ')[1][:-1].split('=')[1])
        py = int(lines[2].split(' ')[2].split('=')[1])

        validx = []
        txa = math.ceil(px / ax)
        txb = 0

        while True:
            print(validx)
            res = ax * txa + bx * txb
            if txa <= 0:
                break
            if res == px:
                validx.append((txa, txb))
            if res > px:
                txa -= 1
            else:
                txb += 1

        validy = [x for x in validx if ay * x[0] + by * x[1] == py]
        print(validy)

        if len(validy) > 0:
            last = validy[-1]
            total += last[0] * 3 + last[1] * 1

    print(total)


def part2():
    data = open('13.txt').read().strip()

    total = 0
    sections = data.split('\n\n')
    for section in sections:
        lines = section.split('\n')
        a = lines[0].split(' ')
        ax = int(a[2][:-1].split('+')[1])
        ay = int(a[3].split('+')[1])
        b = lines[1].split(' ')
        bx = int(b[2][:-1].split('+')[1])
        by = int(b[3].split('+')[1])
        px = int(lines[2].split(' ')[1][:-1].split('=')[1]) + 10000000000000
        py = int(lines[2].split(' ')[2].split('=')[1]) + 10000000000000

        a = Int('a')
        b = Int('b')
        
        score = 3 * a + b
    
        o = Optimize()
        o.add(a * ax + b * bx == px)
        o.add(a * ay + b * by == py)
        o.add(a >= 0)
        o.add(b >= 0)
        o.minimize(score)

        if o.check() == sat:
            m = o.model()
            total += m[a].as_long() * 3 + m[b].as_long() * 1
    print(total)
# part1()
part2()