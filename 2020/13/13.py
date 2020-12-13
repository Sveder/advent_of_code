input = """1000677
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"""
#
# input = """939
# 7,13,x,x,59,x,31,19"""

input = input.split("\n")

original_start = start = int(input[0])

busses = [int(i) for i in input[1].split(",") if i != "x"]

# print(start, busses)
#
# found = False
# bus = None
#
# while not found:
#     for i in busses:
#         if start % i == 0:
#             print("Part1: Bus is:", i, " time is", start)
#             bus = i
#             found = True
#
#     start += 1
#

found = False
offset = 100000000000000 - 1
offset = 100000293078000
offset = 100000510800000 - 2
busses = [int(i) for i in input[1].replace('x', '0').split(",")]
timestamps = []

max = max(busses)
max_index = busses.index(max)
offset = -max_index
offset = 200000000000000 - 200000000000000 % max - max_index

import time
start = time.time()
while not found:
    offset += max

    if offset % 100000 == 0:
        print("offset:", offset)

    local_found = True

    for i, bus_num in enumerate(busses):
        if bus_num == 0:
            continue

        place = offset + i

        if place % bus_num != 0:
            local_found = False
            break

    if local_found:
        found = True
        print("Found it:", offset)


# This took around 5 hours lol
print("Took:", time.time() - start)

# Can also use this to put this in wolfram alpha:
wolfram = ""
for i, num in enumerate(input.split(",")):
    if num != 'x':
        wolfram += "(x + %s) mod %s = 0, " % (i, num)

