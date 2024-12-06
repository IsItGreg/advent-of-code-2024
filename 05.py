
from functools import cmp_to_key


def part1():
    with open('05.txt', 'r') as file:
        data = file.read()

    [rules, updates] = data.split('\n\n')

    rules = rules.split('\n')
    rules = [rule.split('|') for rule in rules]

    ruleMap = {}
    for rule in rules:
        if rule[0] not in ruleMap:
            ruleMap[rule[0]] = set()
        ruleMap[rule[0]].add(rule[1])

    updates = updates.split('\n')

    sum = 0
    for update in updates:
        badRow = False
        update = update.split(',')
        for i in range(len(update)):
            cur = update[i]
            before = set(update[:i])
            if cur in ruleMap:
                if len(ruleMap[cur] & before) > 0:
                    badRow = True
                    break
        if not badRow: 
            sum += int(update[len(update)//2])

    print(sum)

def part2():
    with open('05.txt', 'r') as file:
        data = file.read()

    [rules, updates] = data.split('\n\n')

    rules = rules.split('\n')
    rules = [rule.split('|') for rule in rules]

    ruleMap = {}
    for rule in rules:
        if rule[0] not in ruleMap:
            ruleMap[rule[0]] = set()
        ruleMap[rule[0]].add(rule[1])

    def comparator(a, b):
        if a in ruleMap and b in ruleMap[a]:
            return 1
        if b in ruleMap and a in ruleMap[b]:
            return -1
        return 0
    
    updates = updates.split('\n')

    sum = 0
    for update in updates:
        badRow = False
        update = update.split(',')
        for i in range(len(update)):
            cur = update[i]
            before = set(update[:i])
            if cur in ruleMap:
                if len(ruleMap[cur] & before) > 0:
                    badRow = True
                    break
        if badRow:
            update.sort(key=cmp_to_key(comparator))
            # print(update)
            sum += int(update[len(update)//2])

    print(sum)

part1()
part2()