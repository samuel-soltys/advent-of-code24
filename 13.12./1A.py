sum = 0

with open('./13.12./input.txt', 'r') as f:
    for l in f:
        l = l.replace(",", "").replace("+", "").replace("=", "").replace("X", "").replace("Y", "")
        if "A" in l:
            a_x, a_y = map(int, l.strip("Button A: ").split())
        elif "B" in l:
            b_x, b_y = map(int, l.strip("Button B: ").split())
        elif "Prize: "  in l:
            prize_x, prize_y = map(int, l.strip("Prize: ").split())
        
        if l == "\n":
            solutions = []
            for i in range(0, 100):
                for j in range(0, 100):
                    if (a_x * i + b_x * j) == prize_x and (a_y * i + b_y * j) == prize_y:
                        print(i, j)
                        solutions.append(i * 3 + j)
            if len(solutions) != 0:
                sum += min(solutions)
print(sum)
            