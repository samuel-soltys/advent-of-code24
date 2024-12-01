from collections import defaultdict
sum = 0
l1 = []
l2 = []
s1 = defaultdict(int)
s2 = defaultdict(int)

with open('./1.12./input.txt', 'r') as f:
    for line in f:
        a = int(line.split(" ")[0])
        b = int(line.split(" ")[3].strip("\n"))
        s1[a] += 1
        s2[b] += 1
        l1.append(a)
        l2.append(b)

sum = 0
for i in range(len(l1)):
    if l1[i] in s2:
        sum += l1[i] * s2[l1[i]]

print(sum)