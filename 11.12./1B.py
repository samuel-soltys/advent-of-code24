from collections import defaultdict

a = defaultdict(int)

with open('./11.12./input.txt', 'r') as f:
    for l in f:
        l = l.split()
        for n in l:
            a[n] = 1

for times in range(75):
    a_new = defaultdict(int)
    for n in list(a):
        if n == "0":
            a_new["1"] += a[n]
        elif len(n) % 2 == 0:
            left = str(int(n[0 : len(n) // 2]))
            right = str(int(n[len(n) // 2 : len(n)]))
            a_new[left] += a[n]
            a_new[right] += a[n]
        else:
            a_new[str(int(n) * 2024)] += a[n]
    a = a_new

print(sum(a.values()))