from math import prod

def monkey_business(rounds, divisor):
    #[0] [items]; [1] "first operator second"; [2] divisor; [3] [true, false]; [4] monkey business level
    monkeys = []

    with open("aoc_22_11_input.txt") as file:
        #parse input
        monkey = []
        for line in file.readlines():
            line = line.split()
            if not line:
                continue
            elif line[0] == "Monkey":
                monkey = []
                continue
            elif line[0] == "Starting":
                monkey.append([int(item.strip(",")) for item in line[2:]])
                continue
            elif line[0] == "Operation:":
                monkey.append(" ".join([x for x in line[3:]]))
                continue
            elif line[0] == "Test:":
                monkey.append(int(line[3]))
                continue
            elif line[1] == "true:":
                monkey.append([int(line[5])])
                continue
            elif line[1] == "false:":
                monkey[3].append(int(line[5]))
                monkey.append(0)
                monkeys.append(monkey)
    
    common = prod([monkeys[x][2] for x in range(len(monkeys))])

    for r in range(1, rounds + 1):
        for i in range(len(monkeys)):
            for item in monkeys[i][0]:
                #inspect and operate
                old = item
                item = eval(monkeys[i][1])
                
                item = int(item / divisor)

                item = item % common
               
                #test and throw
                test = item % monkeys[i][2]
                if not test:
                    monkeys[monkeys[i][3][0]][0].append(item)
                else:
                    monkeys[monkeys[i][3][1]][0].append(item)

                #monkey business
                monkeys[i][4] += 1
                    
            monkeys[i][0] = []
    
    return prod(sorted([monkeys[i][4] for i in range(len(monkeys))])[-2:])

#FIRST PART
print(monkey_business(20, 3))

#SECOND PART
print(monkey_business(10000, 1))




