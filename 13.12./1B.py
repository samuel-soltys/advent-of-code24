from sympy.solvers import solve
from sympy import var, Eq
var('x y')

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
            prize_x += 10000000000000
            prize_y += 10000000000000

            eq1 = Eq(a_x * x + b_x * y, prize_x) 
            eq2 = Eq(a_y * x + b_y * y, prize_y)

            output = solve([eq1,eq2],x,y,dict=True)

            if output[0][x].is_integer and output[0][y].is_integer:
                sum += output[0][x] * 3 + output[0][y]

print(sum)