from collections import defaultdict

grid = []
areas = defaultdict(int)
shapes = []

coordinates = defaultdict(list)

with open('./12.12./inputt.txt', 'r') as f:
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
        horizontal_side_makers_up = []
        horizontal_side_makers_down = []
        vertical_side_makers_left = []
        vertical_side_makers_right = []
        for x, y in shape:
            if (x, y - 1) not in shape:
                horizontal_side_makers_up.append((x, y))
            if (x, y + 1) not in shape:
                horizontal_side_makers_down.append((x, y))
            if (x - 1, y) not in shape:
                vertical_side_makers_left.append((x, y))
            if (x + 1, y) not in shape:
                vertical_side_makers_right.append((x, y))

        to_remove = set()
        for pair in horizontal_side_makers_up:
            x, y = pair
            for pair2 in horizontal_side_makers_up:
                x2, y2 = pair2
                if x2 - x == 1 and y2 == y:
                    to_remove.add(pair2)
        for pair in to_remove:
            horizontal_side_makers_up.remove(pair)

        to_remove = set()
        for pair in horizontal_side_makers_down:
            x, y = pair
            for pair2 in horizontal_side_makers_down:
                x2, y2 = pair2
                if x2 - x == 1 and y2 == y:
                    to_remove.add(pair2)
        for pair in to_remove:
            horizontal_side_makers_down.remove(pair)

        to_remove = set()
        for pair in vertical_side_makers_left:
            x, y = pair
            for pair2 in vertical_side_makers_left:
                x2, y2 = pair2
                if y2 - y == 1 and x2 == x:
                    to_remove.add(pair2)
        for pair in to_remove:
            vertical_side_makers_left.remove(pair)

        to_remove = set()
        for pair in vertical_side_makers_right:
            x, y = pair
            for pair2 in vertical_side_makers_right:
                x2, y2 = pair2
                if y2 - y == 1 and x2 == x:
                    to_remove.add(pair2)
        for pair in to_remove:
            vertical_side_makers_right.remove(pair)

        num_sides = len(vertical_side_makers_right) + len(vertical_side_makers_left) + len(horizontal_side_makers_up) + len(horizontal_side_makers_down)
        sum += len(shape) * num_sides
    final_sum += sum

print(final_sum)