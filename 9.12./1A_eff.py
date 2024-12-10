import re 
# from collections import defaultdict
import time
blocks = []
nums = []
sum = 0
with open('./9.12./input.txt', 'r') as f:
    for l in f:
        l = list(l)
        index = 0
        for i in range(len(l)):
            if i % 2 == 0:
                # s += int(l[i])
                if int(l[i]) != 0:
                    blocks.append(str(index) * int(l[i]))
                for n in range(int(l[i])):
                    nums.append(str(index))
                index += 1
            else:
                if int(l[i]) != 0:
                    blocks.append("." * int(l[i]))
                for n in range(int(l[i])):
                    nums.append(".")
    a = list(blocks)

# print(s)
ra = [i for i in reversed(a) if "." not in i]

index = 0
while index < len(ra) - 1:
    for i in range(len(a)):
        if "." in blocks[i]:
            if len(blocks[i]) > len(ra[index]):
                if blocks.index(ra[index]) > i:

                    a[blocks.index(ra[index])] = "." * len(ra[index])
                    for i in range(len(ra[index])):
                        nums[blocks.index(ra[index])] = "."

                    blocks.insert(i + 1, "." * (len(blocks[i]) - len(ra[index])))
                    for n in range((len(blocks[i]) - len(ra[index]))):
                        nums.insert(i + 1, ".")
                    
                    blocks[i] = ra[index]

                    index += 1

            elif len(blocks[i]) == len(ra[index]):
                if blocks.index(ra[index]) > i:

                    blocks[blocks.index(ra[index])] = "." * len(ra[index])
                    blocks[i] = ra[index]

                    index += 1
    index += 1
# # print("".join(blocks[s:]))

# result = re.findall(str(num), string)
# num = 0
# for i in range(len(ra)):
#     if "." not in blocks[i]:
#         blocks[i] = blocks[i].split(str(num))
#         num += 1
#         # sum += i * int(blocks[i])
print(a)
with open('./9.12./test.txt', 'w') as f:
    f.write("".join(a))
    