with open('./11.12./input.txt', 'r') as f:
    for l in f:
        a = l.split()

for n in range(25):
    i = 0
    length = len(a)
    while i < length:
        if a[i] == "0":
            a[i] = "1"
        elif len(a[i]) % 2 == 0:
            left = str(int(a[i][0 : len(a[i]) // 2]))
            right = str(int(a[i][len(a[i]) // 2 : len(a[i])]))
            a[i] = left
            a.insert(i + 1, right)
            length += 1
            i += 1
        else:
            a[i] = str(int(a[i]) * 2024)
        i += 1

print(len(a))