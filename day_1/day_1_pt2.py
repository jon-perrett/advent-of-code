"""
Take input list of integers and return the product of the three that sum to 2020
"""

import csv

with open("day_1_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    d = list(reader)

ds = [int(i[0]) for i in d]

def adds_to_x(x,input):
    for i,v in enumerate(input):
        for j,u in enumerate(input):
            for k,t in enumerate(input):
                if (i!=j) and (i!=k) and (j!=k) and (v+u+t == x):
                    print(v*u*t)
                        

adds_to_x(2020,ds)
