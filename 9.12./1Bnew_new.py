a = []
dot_blocks_len = []
num_blocks_len = []
with open('./9.12./inputt.txt','r') as f:
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
num_block_index = len(num_blocks_len) - 1
# while num_block_index >= 0:
i = 0
while i < sum(num_blocks_len):
    print("".join(a))
    if a[i] == ".":
        found = False
        for ind in range(num_block_index, -1, -1):
            dot_block_len = dot_blocks_len[dot_block_index]
            num_block_len = num_blocks_len[ind]
            while a[back_index] == ".":
                back_index -= 1
            if num_block_len <= dot_block_len:
                for j in range(i, i + num_block_len):
                    if j < back_index:
                        a[j] = a[back_index]
                        a[back_index] = "."
                        back_index -= 1
                found = True
                # back_index -= num_block_len
                break
            back_index -= num_block_len + 1
            # num_block_index -= 1

                
            # elif num_block_len == dot_block_len:
            #     print("dot_len", dot_block_len)
            #     print("num_len", num_block_len)

        i += dot_blocks_len[dot_block_index] - 1
        dot_block_index += 1
        num_block_index = ind - 1

    i += 1
    # num_block_index -= 1