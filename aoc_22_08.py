from functools import reduce

with open("aoc_22_08_input.txt") as file:
    grid = [line.strip("\n") for line in file.readlines()]
    
    # Total number of trees
    total = 0
    max_score = 0

    # Loop through each number in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total += 1
            invisibility = 0
            scenic_score = [0,0,0,0]

            # Check if there is any higher tree to the left of the current tree
            if j > 0:
                for k in range(j-1, -1, -1):
                    scenic_score[0] += 1
                    if grid[i][k] >= grid[i][j]:
                        invisibility += 1
                        break

            # Check if there is any higher tree to the right of the current tree
            if j < len(grid[i]) - 1:
                for k in range(j+1, len(grid[i])):
                    scenic_score[1] += 1
                    if grid[i][k] >= grid[i][j]:
                        invisibility += 1
                        break

            # Check if there is any higher tree above the current tree
            if i > 0:
                scenic_count = 0
                for k in range(i-1, -1, -1):
                    scenic_score[2] += 1
                    if grid[k][j] >= grid[i][j]:
                        invisibility += 1
                        break

            # Check if there is any higher tree below the current tree
            if i < len(grid) - 1:
                scenic_count = 0
                for k in range(i+1, len(grid)):
                    scenic_score[3] += 1
                    if grid[k][j] >= grid[i][j]:
                        invisibility += 1
                        break
                    
            # FIRST PART
            # Total number of trees minus the ones hidden from all four sides
            if invisibility == 4:
                total -= 1

            #SECOND PART
            scenic_score = reduce(lambda x, y: x*y, scenic_score)
            if scenic_score > max_score:
                max_score = scenic_score

    print(total)
    print(max_score)