#FOR SECOND PART JUST REVERSE THE LOAD LIST BELOW

import re

with open("aoc_22_05_input.txt") as file:
    line = file.readline()
    
    #create empty stacks
    stacks = []
    for i in range(len(line)//4):
        stacks.append([])

    #populate stacks with crates
    while line:
        if line == "\n":
            for stack in stacks:
                stack.reverse()
            line = file.readline()
            break
        else:
            for i, c in enumerate(line):
                if c.isalpha():
                    stacks[i // 4].append(c)
        line = file.readline()

    #get instructions and move crates
    while line:
        # index 0 -> number of crates; index 1 -> move from; index 2 -> move to 
        instructions = re.findall(r"\b\d+\b", line)

        load = []
        for i in range(int(instructions[0])):
            load.append(stacks[int(instructions[1])-1].pop())
        
        #SECOND PART
        #load.reverse()
        
        for crate in load:
            stacks[int(instructions[2])-1].append(crate)

        line = file.readline()

    #get result
    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)


        
        


    