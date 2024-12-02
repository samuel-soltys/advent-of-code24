valid_lines = 0

with open('./2.12./input.txt', 'r') as f:
    for line in f:
        numbers = line.split(" ")
        for i in range(len(numbers)): numbers[i] = int(numbers[i])
        
        # If decreasing
        if numbers[0] > numbers[1]:
            valid_nums = 0
            for i in range(len(numbers) - 1):
                if numbers[i] - numbers[i + 1] in range(1, 4):
                    valid_nums += 1
            if valid_nums == len(numbers) - 1:
                valid_lines += 1
        
        # If increasing
        elif numbers[0] < numbers[1]:
            valid_nums = 0
            for i in range(len(numbers) - 1):
                if numbers[i] - numbers[i + 1] in range(-3, 0):
                    valid_nums += 1
            if valid_nums == len(numbers) - 1:
                valid_lines += 1

print(valid_lines)