a = []
dot_blocks_len = []
num_blocks_len = []
with open('./9.12./input.txt','r') as f:
    for l in f:
        l = list(l)
        index = 0
        for i in range(len(l)):
            if i % 2 == 0:
                num_blocks_len.append(int(l[i]))
                for n in range(int(l[i])):
                    a.append(str(index))
                index += 1
            else:
                dot_blocks_len.append(int(l[i]))
                for n in range(int(l[i])):
                    a.append(".")

print(num_blocks_len, dot_blocks_len)

dot_block_index = 0
back_index = len(a) - 1
i = 0
while i < sum(num_blocks_len):
    # print("".join(a))
    if a[i] == ".":
        for j in range(i, i + dot_blocks_len[dot_block_index]):
            # print(a[j], end=" ")
            while a[back_index] == ".":
                back_index -= 1
            
            a[j] = a[back_index]
            a[back_index] = "."
            back_index -= 1

        i += dot_blocks_len[dot_block_index] - 1
        dot_block_index += 1
    i += 1
