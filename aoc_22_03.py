result = 0
result_2 = 0
threes = []

with open("aoc_22_03_input.txt") as file:
    for line in file.readlines():
        line = line.strip("\n")
        #FIRST PART
        first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
        item = ord(str(first & second)[2])
        result += item - 96 if (97 <= item) else item - 38

        #SECOND PART
        threes.append(set(line))
        if len(threes) == 3:
            item_2 = ord(str((threes[0] & threes[1]) & threes[2])[2])
            result_2 += item_2 - 96 if (97 <= item_2) else item_2 - 38
            threes = []
        
print(result)
print(result_2)
