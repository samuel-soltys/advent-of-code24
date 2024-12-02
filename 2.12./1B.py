sum = 0
with open('./2.12./input.txt', 'r') as f:
    for line in f:
        numbers = line.split(" ")  
        for i in range(len(numbers)): numbers[i] = int(numbers[i])
        
        without_tolerance = False
        # If decreasing
        if numbers[0] > numbers[1]:
            valid_nums = 0
            for i in range(len(numbers) - 1):
                if numbers[i] - numbers[i + 1] in range(1, 4):
                    valid_nums += 1
            if valid_nums == len(numbers) - 1:
                sum += 1
                without_tolerance = True
        # If increasing
        elif numbers[0] < numbers[1]:
            valid_nums = 0
            for i in range(len(numbers) - 1):
                if numbers[i] - numbers[i + 1] in range(-3, 0):
                    valid_nums += 1
            if valid_nums == len(numbers) - 1:
                sum += 1
                without_tolerance = True
        
        if not without_tolerance:
            for index in range(len(numbers)):
                numbers_removed = list(numbers)
                numbers_removed[index] = " "
                numbers_removed.remove(" ")
                # If decreasing
                if numbers_removed[0] > numbers_removed[1]:
                    valid_nums = 0
                    for i in range(len(numbers_removed) - 1):
                        if numbers_removed[i] - numbers_removed[i + 1] > 0 and numbers_removed[i] - numbers_removed[i + 1] <= 3:
                            valid_nums += 1
                    if valid_nums == len(numbers_removed) - 1:
                        sum += 1
                        break
                # If increasing
                elif numbers_removed[0] < numbers_removed[1]:
                    valid_nums = 0
                    for i in range(len(numbers_removed) - 1):
                        if numbers_removed[i] - numbers_removed[i + 1] < 0 and numbers_removed[i] - numbers_removed[i + 1] >= -3:
                            valid_nums += 1
                    if valid_nums == len(numbers_removed) - 1:
                        sum += 1
                        break
print(sum)