def find_packet(string, x):
    for i in range((x - 1), len(string)):
        packet = {buffer[y] for y in range((i - (x - 1)), (i + 1))}
        if len(packet) == (x):
            return (i + 1)

with open("aoc_22_06_input.txt") as file:
    buffer = file.read().strip("\n")
    #FIRST PART
    print(find_packet(buffer, 4))
    #SECOND PART
    print(find_packet(buffer, 14))

        
        