nums = []
length_dot_blocks = []
length_num_blocks = []
with open('./9.12./inputt.txt', 'r') as f:
    for l in f:
        l = list(l)
        index = 0
        for i in range(len(l)):
            if i % 2 == 0:
                length_num_blocks.append(int(l[i]))
                # s += int(l[i])
                for n in range(int(l[i])):
                    nums.append(str(index))
                index += 1
            else:
                length_dot_blocks.append(int(l[i]))
                for n in range(int(l[i])):
                    nums.append(".")
# print(s)
# r_nums = [i for i in reversed(nums) if i != "."]
index = 0
block_num = 0


r_index = 0
while index < len(nums):
    # print("".join(nums))
    if nums[index] == ".":
        length_dot_block = length_dot_blocks[block_num]
        length_num_block = length_num_blocks[-(block_num + 1)]

        # print(length_dot_block, length_num_block)
        if length_dot_block >= length_num_block:
            # for i in block_num:

            print(r_nums[r_index : r_index + length_num_block])
        # for n in range(block_num):
            print(r_index)
            r_index += length_num_blocks[block_num]
        block_num += 1
        # elif length_dot_block == length_num_block:

            # for i in range(index, index + length_num_block):
                # nums[i] = r_nums[r_index]
        #         r_index += 1
        # elif length_dot_block == length_num_block:
        #     for i in range(index, index + length_num_block):
        #         nums[i] = r_nums[r_index]
        #         r_index += 1
    index += 1
    
print(nums)    
