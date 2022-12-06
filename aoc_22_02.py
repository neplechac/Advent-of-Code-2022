shapes = ["ABC", "XYZ"]
win = [1, 2, 0]
loss = [2, 0, 1]
score_1 = 0
score_2 = 0

def calc_score(opponent, you):
    game = opponent - you
    score = 0

    #win
    if game in (2, -1):
        score += 6
    #draw
    if game == 0:
        score += 3

    score += (second + 1)
    return score

with open("aoc_22_02_input.txt") as file:
    for line in file.readlines():
        first = shapes[0].index(line[0])
        second = shapes[1].index(line[2])

        #FIRST PART
        score_1 += calc_score(first, second)

        #SECOND PART
        if second == 2:
            second = win[first]
        elif second == 0:
            second = loss[first]
        else:
            second = first
        score_2 += calc_score(first, second)

print(score_1, score_2)
