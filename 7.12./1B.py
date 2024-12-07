import itertools

sum = 0

with open('./7.12./input.txt', 'r') as f:
    for l in f:
        test, nums = l.split(":")
        test = int(test)
        nums = nums.split()
        nums[-1].strip("\n")
        for i in range(len(nums)): nums[i] = int(nums[i])
        
        # itertools.permutations(["*", "*"], len(nums))
        all_perms = list(itertools.product(["*","+", "||"], repeat=len(nums) - 1))
        for perm in all_perms:
            result = nums[0]
            for i in range(len(perm)):
                if perm[i] == "+":
                    result += nums[i + 1]
                elif perm[i] == "*":
                    result *= nums[i + 1]
                elif perm[i] == "||":
                    result = str(result) + str(nums[i + 1])
                    result = int(result)
            if result == test:
                sum += test
                break
            
print(sum)