#This one is bit of a mess

def check_node(queue, discovered, steps, prev, x, y):
    #end condition
    if grid[prev[0]][prev[1]] == "z" and grid[y][x] == "E":
        steps.append((prev[2] + 1))
    #add relevant non-discovered nodes to queue
    if ord(grid[prev[0]][prev[1]]) + 1 >= ord(grid[y][x]) and (y, x) not in discovered:
        discovered.add((y, x))
        queue.append([y, x, prev[2] + 1])

def find_path(starting_points):
    #no. of steps for each path
    steps = []
    
    #find path for every starting point
    for start in starting_points:
        queue = [start]
        discovered = set()
        discovered.add((start[0], start[1]))
        
        # while there are undiscovered nodes
        while queue:
            current = queue[0]

            #check left
            if current[1] > 0:
                check_node(queue, discovered, steps, current, current[1] - 1, current[0])
                
            #check right
            if current[1] < len(grid[current[0]]) - 1:
                check_node(queue, discovered, steps, current, current[1] + 1, current[0])

            #check above
            if current[0] > 0:
                check_node(queue, discovered, steps, current, current[1], current[0] - 1)

            #check below
            if current[0] < (len(grid)) - 1:
                check_node(queue, discovered, steps, current, current[1], current[0] + 1)
            
            del queue[0]
    
    # return the lowest number of steps   
    return min(steps)

with open("aoc_22_12_input.txt") as file:
    grid = [line.strip("\n") for line in file.readlines()]

    #find starting points
    starting_points = []
    for i in range(len(grid)):
        if not grid[i].find("S"):
            start = [i, grid[i].find("S"), 0]
            grid[start[0]] = grid[start[0]][:0] + "a" + grid[start[0]][1:]
        for j in range(len(grid[i])):
            if grid[i][j] == "a":
                starting_points.append([i, j, 0])
    
    #FIRST PART
    print(find_path([start]))

    #SECOND PART
    print(find_path(starting_points))
    

    



 