input = """0,3,1,6,7,5"""

# input = """0,3,6"""
# input = """1,3,2"""

input = [int(i) for i in input.split(",")]
end = 2020
end = 30000000

turn = len(input) - 1
d = {number: index for index, number in enumerate(input)}

for i in range(turn, end):
    # if i % 10000 == 0:
    #     print("i = ", i)

    last_num = input[-1]
    cur_num = None

    if last_num in d.keys():
        last_index = d[last_num]
        cur_num = i - last_index
        d[last_num] = i

    else:
        d[last_num] = i
        cur_num = 0

    # print(i, last_num, cur_num, d, input)
    input.append(cur_num)

    #import pdb;pdb.set_trace()

    # #Original part 1, seems slowish for part 2:
    # last_num = input[i - 1]
    #
    # if input.count(last_num) == 1:
    #     input.append(0)
    #     continue
    #
    # reversed = input[::-1]
    # last = reversed.index(last_num)
    # almost_last = reversed.index(last_num, last +1 )
    #
    # input.append(abs(last - almost_last))


# print(input)
print("--->", input[-2])