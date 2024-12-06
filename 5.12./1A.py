from collections import defaultdict
sum = 0
rules = defaultdict(list)
switch = False
updates = []
valid = []

with open('./5.12./input.txt', 'r') as f:
    for l in f:
        if l == "\n":
            switch = True
        elif not switch:
            number, after = l.split("|")
            rules[int(number)].append(int(after.strip("\n")))
        else:
            update = l.split(",")
            update[-1].strip("\n")
            for i in range(len(update)): update[i] = int(update[i])
            updates.append(update)

for u in updates:
    valid_sequence = True
    for i in range(1, len(u)):
        for j in range(0, i):
            if u[j] in rules[u[i]]:
                valid_sequence = False
    if valid_sequence:
        valid.append(u)

for u in valid:
    sum += u[len(u) // 2]

print(sum)