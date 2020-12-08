"""
Take input list of integers and return the product of the pair that sum to 2020
"""


import csv

with open("day_1_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    d = list(reader)

ds = [int(i[0]) for i in d]

def adds_to_x(x,input):
    for i,v in enumerate(input):
        for j,u in enumerate(input):
            if (i!=j) and (v+u == x):
                print(v*u)
                        

adds_to_x(2020,ds)
