tree = {}
path = []

with open("aoc_22_07_input.txt") as file:
    for line in file.readlines():
        line = line.split()
        
        #get current path
        if line[1] == "cd":
            if line[2] == "..":
                del path[-1]
            elif line[2] == "/":
                path = ["/"]
            else:
                path.append(line[2])

        #directory tree
        if line[0].isnumeric():
            dir_path = ""
            for directory in path:
                dir_path += directory
                if dir_path not in tree:
                    tree[dir_path] = int(line[0])
                else:
                    tree[dir_path] += int(line[0])
    
    #FIRST PART
    print(sum(v for v in tree.values() if v <= 100000)) 

    #SECOND PART
    space_needed = 30000000 - (70000000 - tree["/"])
    print(min(v for v in tree.values() if v >= space_needed))






        
