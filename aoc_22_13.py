from ast import literal_eval
from math import prod
from functools import cmp_to_key

def compare(l, r):
    #both are integers
    if type(l) == int and type(r) == int:
        return l - r
    # both are lists
    elif type(l) == list and type(r) == list:
        for i, j in zip(l, r):
            x = compare(i, j)
            if x != 0:
                return x
        return compare(len(l), len(r))
    #different types, convert the int to list
    elif type(l) == int and type(r) == list:
        return compare([l], r)
    elif type(l) == list and type(r) == int:
        return compare(l, [r])
    
with open("aoc_22_13_input.txt") as file:
    packets = [literal_eval(line.strip()) for line in file.readlines() if len(line.strip())]
    
    #FIRST PART
    result_1 = 0

    for i, (left, right) in enumerate(zip(packets[::2], packets[1::2])):
        if compare(left, right) <= 0:
            result_1 += i + 1
        
    print(result_1)

    #SECOND PART
    dividers = [[[2]], [[6]]]
    result_2 = []

    for i, packet in enumerate(sorted(packets + dividers, key=cmp_to_key(compare))):
        if packet in dividers:
            result_2.append(i + 1)
    
    print(prod(result_2))

            

     




