import re
sum = 0
with open('./3.12./input.txt', 'r') as f:
    for s in f:
        match = re.findall("mul\(([0-9]+),([0-9]+)\)", s)
        for n in match:
            sum += int(n[0]) * int(n[1])
print(sum)