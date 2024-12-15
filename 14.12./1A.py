quadrants = [0, 0, 0, 0]

with open('./14.12./input.txt', 'r') as f:
    for l in f:
        l = l.strip("\n").replace("p=", "").replace("v=", "").split(" ")
        p = list(map(int, l[0].split(",")))
        v = list(map(int, l[1].split(",")))
        
        for s in range(100):
            p[0] += v[0]
            p[0] %= 101
            if p[0] < 0:
                p[0] = 101 + p[0]
            
            p[1] += v[1]
            p[1] %= 103
            if p[1] < 0:
                p[1] = 103 + p[1]
            

        if p[0] > 50 and p[1] > 51:
            quadrants[0] += 1
        elif p[0] < 50 and p[1] > 51:
            quadrants[1] += 1
        elif p[0] < 50 and p[1] < 51:
            quadrants[2] += 1
        elif p[0] > 50 and p[1] < 51:
            quadrants[3] += 1
sum = quadrants[0]
for i in range(1, 4):
    sum *= quadrants[i]

print(sum)