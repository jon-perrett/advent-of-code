import csv

with open(r"day_5\day_5_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    lines = list(reader)

lines = [l[0] for l in lines]

def FindSeatID(input):    
    range_pos_min = 0
    range_pos_max = 128 # 1 indexed

    lateral_pos_min = 0
    lateral_pos_max = 8

    for pos in range(len(input)):
        if input[pos] == "F":
            # take front half
            range_pos_max -= int((range_pos_max-range_pos_min)/2 )
            range_pos_min = range_pos_min
        elif input[pos] == "B":
            range_pos_max = range_pos_max
            range_pos_min +=  int((range_pos_max-range_pos_min)/2)
        elif input[pos] == "L":
            lateral_pos_max -= int((lateral_pos_max-lateral_pos_min)/2)
            lateral_pos_min = int(lateral_pos_min)
        elif input[pos] == "R":
            lateral_pos_max = lateral_pos_max
            lateral_pos_min += int((lateral_pos_max-lateral_pos_min)/2)
    
    pos_long = range(range_pos_min,range_pos_max)[0]
    pos_lat = range(lateral_pos_min,lateral_pos_max)[0]

    return pos_long * 8 + pos_lat

max = 0
for l in lines:
    ids = FindSeatID(l)
    if ids > max:
        max = ids
print(max)
