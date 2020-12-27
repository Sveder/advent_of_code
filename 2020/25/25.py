input = """11349501
5107328"""

# input = """5764801
# 17807724"""


magic_mod = 20201227


def transform(subject, loop_size):
    res = 1

    for i in range(loop_size):
        res *= subject
        res %= magic_mod

    return res

def find_loop_size(subject, target):
    res = 1

    for i in range(1, 200000000000):
        res *= subject
        res %= magic_mod

        if res == target:
            return i

    return None


first, second = input.split('\n')
first, second = int(first), int(second)

first_loop_size = find_loop_size(7, first)
second_loop_size = find_loop_size(7, second)

#
# #
# for f in range(1, 2000):
#     for s in range(1, 200):
#         if transform(first, s) == transform(second, f):
#             print(f, s, transform(first, s))
#             import pdb;pdb.set_trace()
#
# #             # 601 193 9902402

# for i in range(2000000):
#     if i % 10000 == 0:
#         print("I", i)
#
#     if transform(i, 11) == second:
#         print('Hi there', i)

print(first_loop_size, second_loop_size)

print(transform(first, second_loop_size), '=', transform(second, first_loop_size))