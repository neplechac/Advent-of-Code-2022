from math import sqrt

def distance(knot_a, knot_b):
    return sqrt((knot_a[0] - knot_b[0])**2 + (knot_a[1] - knot_b[1])**2)

def direction(prev, new):
    return[(prev[0] - new[0]), (prev[1] - new[1])]

def calculate_moves(knots):
    rope = [[0,0] for knot in range(knots)]
    rope_next = [[0,0] for knot in range(knots)]
    tail_moves = [[0,0]]
    
    for line in file.readlines():
        line = line.split()
        for m in range(int(line[1])):
            if line[0] == "R":
                move = (0, 1)
            if line[0] == "L":
                move = (0, -1)
            if line[0] == "U":
                move = (1, 1)
            if line[0] == "D":
                move = (1, -1)
            
            # move head
            rope_next[0][move[0]] += move[1]
            
            # first knot
            if distance(rope_next[0], rope[1]) >= 2:
                rope_next[1] = rope[0][:]
            
            # other knots
            if knots > 2:
                for i in range(2, knots):
                    prev_move = direction(rope_next[i-1], rope[i-1])

                    # same row or column
                    if distance(rope_next[i-1], rope[i]) == 2:
                        diff = direction(rope_next[i-1], rope[i])
                        for j in range(len(diff)):
                            rope_next[i][j] += diff[j] / 2

                    # different row and column    
                    elif distance(rope_next[i-1], rope[i]) > 2:
                        if distance(rope_next[i-1], rope[i-1]) == 1:
                            rope_next[i] = rope[i-1][:]
                        else:
                            rope_next[i][0] += prev_move[0]
                            rope_next[i][1] += prev_move[1]
            
            rope = [x[:] for x in rope_next]
            tail_moves.append(rope[-1][:])
            
    return len({tuple(x) for x in tail_moves})

with open("aoc_22_09_input.txt") as file:
    print(calculate_moves(10))
    