sum = 0
l1 = []
l2 = []

with open('./1.12./input.txt', 'r') as f:
    for line in f:
        a = int(line.split(" ")[0])
        b = int(line.split(" ")[3].strip("\n"))
        l1.append(a)
        l2.append(b)

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])

print(sum)