import csv
import re
with open(r"day_4\day_4_input.txt") as f:
    reader = csv.reader(f,delimiter="\n")
    lines = list(reader)

req_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
optional_fields = ["cid"]

# split lines into groups of properties
groups = []
tmp = []
for i in lines:
    if i:
        tmp.append(i)
    else:
        groups.append(tmp)
        tmp=[]
groups.append(tmp)

ss = []
for g in groups:
    s = ""
    for f in g:
        s+=" " + f[0] + " "
    ss.append(s)

passes = []
for s in ss:
    if all(x in s for x in req_fields):
        passes.append(s)

eye_colours = ["amb","blu","brn","gry","grn","hzl","oth"]

valid = 0
for p in passes:
    splits = p.split()
    bools = [False,False,False,False,False,False,False]
    for s in splits:
        if s.find("byr") != -1:
            val = s.split(":")[1]
            if int(val) >= 1920 and int(val) <= 2002:
                bools[0] = True
            else:
                continue
        if s.find("iyr") != -1:
            val = s.split(":")[1]
            if int(val) >= 2010 and int(val) <= 2020:
                bools[1] = True
            else:
                continue
        if s.find("eyr") != -1:
            val = s.split(":")[1]
            if int(val) >= 2020 and int(val) <= 2030:
                bools[2] = True
            else:
                continue
        if s.find("hgt") != -1:
            val = s.split(":")[1]
            if val.find("cm")!=-1:
                hgt = val.split("cm")[0]
                if int(hgt) >= 150 and int(hgt) <=193:
                    bools[3] = True
            elif val.find("in")!=-1:
                hgt = val.split("in")[0]
                if int(hgt) >= 59 and int(hgt) <=76:
                    bools[3] = True
        if s.find("hcl") != -1:
            val = s.split(":")[1]
            if re.search("^#(?:[0-9a-f]{6})$",val):
                bools[4] = True
            else:
                continue
        if s.find("ecl") != -1:
            val = s.split(":")[1]
            if any(x in val for x in eye_colours):
                bools[5] = True
            else:
                continue
        if s.find("pid") !=-1:
            val = s.split(":")[1]
            if re.search("^([0-9]{9})$",val):
                bools[6] = True
    if all(bools):
        valid+=1

print(valid)

            



# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.


