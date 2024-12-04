import re

sum = 0
with open('./3.12./input.txt', 'r') as f:
    for s in f:
        match = re.findall("mul\(([0-9]+),([0-9]+)\)", s)
        indexes = [m.start() for m in re.finditer("mul\(([0-9]+),([0-9]+)\)", s)]
        
        donts = [m.start() for m in re.finditer("don't\(\)", s)]
        do = [m.start() for m in re.finditer('do\(\)', s)]

        enabled = True
        match_index = 0
        for i in range(len(s)):
            if i in donts:
                enabled = False
            if i in do:
                enabled = True
            if i in indexes:
                if enabled:
                    sum += int(match[match_index][0]) * int(match[match_index][1])
                match_index += 1
print(sum)