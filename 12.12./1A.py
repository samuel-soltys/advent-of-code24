from collections import defaultdict

grid = []
areas = defaultdict(int)
shapes = []

coordinates = defaultdict(list)

with open('./12.12./input.txt', 'r') as f:
    i = 0
    for l in f:
        a = list(l)[:-1]
        for j in range(len(a)):
            coordinates[a[j]].append((i, j))
        i += 1

final_sum = 0
for region in coordinates.keys():
    shapes = [[coordinates[region][0]]]
    while True:
        shape = shapes[-1]
        while True:
            to_add = []
            for x_shape, y_shape in shape:
                for x_add, y_add in coordinates[region]:
                    if (x_add - 1 == x_shape or x_add + 1 == x_shape) and y_add == y_shape:
                        if (x_add, y_add) not in shape and (x_add, y_add) not in to_add:
                            to_add.append((x_add, y_add))
                    elif x_add == x_shape and (y_add - 1 == y_shape or y_add + 1 == y_shape):
                        if (x_add, y_add) not in shape and (x_add, y_add) not in to_add:
                            to_add.append((x_add, y_add))
            if len(to_add) == 0:
                break
            shape.extend(to_add)
        
        found_all = True
        for remaining_pair in coordinates[region]:
            found = False
            for shape in shapes:
                if remaining_pair in shape:
                    found = True
            if not found:
                shapes.append([remaining_pair])
                found_all = False
                break
        if found_all:
            break

    sum = 0
    for shape in shapes:
        perimeter = 0
        for x, y in shape:
            adjacent = 0
            if (x - 1, y) in shape:
                adjacent += 1
            if (x + 1, y) in shape:
                adjacent += 1
            if (x, y - 1) in shape:
                adjacent += 1
            if (x, y + 1) in shape:
                adjacent += 1
            perimeter += 4 - adjacent
        sum += len(shape) * perimeter
    final_sum += sum

print(final_sum)