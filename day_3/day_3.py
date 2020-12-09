import csv
import numpy as np

with open(r"day_3\day_3_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    lines = list(reader)

lines = [l[0] for l in lines]
def hitting_trees(pattern,chars_right,chars_down):
    pos_x = 0
    pos_y = 0 # start at top left
    trees = 0 #initialise at 0 trees
    while pos_y < len(pattern): # check rows down is less than total rows
        if pos_x >= len(pattern[pos_y]):
            pattern[pos_y] += pattern[pos_y]
        else:
            if pattern[pos_y][pos_x] == "#":
                trees += 1
            pos_x += chars_right
            pos_y += chars_down

    return trees

vectors = [[1,1],[3,1],[5,1],[7,1],[1,2]]

prod = 1
for i in vectors:
    prod = prod * hitting_trees(lines,i[0],i[1])

print(prod)




