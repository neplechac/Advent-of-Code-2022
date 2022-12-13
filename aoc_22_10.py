cycle = 1
signal = 1
result = 0
screen = ""

def check_cycle(cycle):
    return cycle * signal if cycle in [20, 60, 100, 140, 180, 220] else 0

def draw(cycle, signal):
    return "#" if (cycle - 1) % 40 in [signal - 1, signal, signal + 1] else "."

with open("aoc_22_10_input.txt") as file:
    for line in file.readlines():
        line = line.split()
        
        #noop
        if line[0] == "noop":
            result += check_cycle(cycle)
            screen += draw(cycle, signal)
            cycle += 1
        #addx
        else:
            for i in range(2):
                result += check_cycle(cycle)
                screen += draw(cycle, signal)
                cycle += 1
            signal += int(line[1])
    
    #FIRST PART
    print(result)

    #SECOND PART
    for row in [screen[i:i+40] for i in range(0, len(screen), 40)]:
        print(row)