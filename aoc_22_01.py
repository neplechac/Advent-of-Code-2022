result = []
temp = 0

with open("aoc_22_01_input.txt") as file:
    line = file.readline()

    while line:
        if line == "\n":
            result.append(temp)
            temp = 0
        else:
            temp += int(line.rstrip("\n"))

        line = file.readline()

# top elf
print(max(result))

# top 3
print(sum(sorted(result, reverse=True)[:3]))
