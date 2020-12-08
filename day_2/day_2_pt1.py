"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
"""

import csv

with open(r"day_2\day_2_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    lines = list(reader)


n_valid = 0
for l in lines:
    s = l[0].split(" ") #split on spaces

    # find number of occurences
    n = s[0] #first split is number of occurences allowed in format min-max, n.
    ns = n.split("-") # split on "-" to find min and max
    n_min = int(ns[0])
    n_max = int(ns[1])

    c = s[1][0] # find policy letter

    password = s[2]

    n_occurences = password.count(c)

    if (n_occurences >= n_min) and (n_occurences <= n_max):
        n_valid+=1
    
print(n_valid)



