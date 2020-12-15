# input = """0,3,1,6,7,5"""

input = """0,3,6"""
# input = """1,3,2"""

input = [int(i) for i in input.split(",")]

turn = len(input)

d = {number: [index] for index, number in enumerate(input)}
last_num = input[-1]

for i in range(turn, 30000000):
    if i % 10000 == 0:
        print("i = ", i)
    #
    # if last_num in d.keys():
    #     indexes = d[last_num]
    #
    # else:
    #     d[last_num] = []



    #import pdb;pdb.set_trace()

    #Original part 1, seems slowish for part 2:
    last_num = input[i - 1]

    if input.count(last_num) == 1:
        input.append(0)
        continue

    reversed = input[::-1]
    last = reversed.index(last_num)
    almost_last = reversed.index(last_num, last +1 )

    input.append(abs(last - almost_last))


print(input)
print(input[30000000-1])