count_1 = 0
count_2 = 0

with open("aoc_22_04_input.txt") as file:
    for line in file.readlines():
        line = line.strip("\n").split(",")
        first, second = line[0].split("-"), line[1].split("-")

        first = set(range(int(first[0]), int(first[1]) + 1))
        second = set(range(int(second[0]), int(second[1]) + 1))

        overlap = first & second 

        #FIRST PART
        if overlap in (first, second):
            count_1 += 1

        #SECOND PART
        if overlap:
            count_2 += 1

print(count_1)
print(count_2)
        