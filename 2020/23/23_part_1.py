class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

input = "253149867"

input = "389125467"

input = [int(i) for i in input] # + list(range(10, 1000000+1))

moves = 100
# moves = 10000000

cur_cup_index = 0

for i in range(moves):
    cur_cup = input[cur_cup_index]
    slice = input[cur_cup_index + 1: cur_cup_index + 4]

    moo = list(input)
    moo[cur_cup_index + 1: cur_cup_index + 4] = []

    if len(slice) != 3:
        from_start = 3 - len(slice)
        moo[:from_start] = []
        slice += input[:from_start]

    if i % 10000 == 0:
        print("Move:", i +1)

    # print('Cups:', input)
    # print('pick ip:', slice)

    dest = cur_cup - 1
    dest_index = None

    while True:
        if dest == 0:
            dest = max(moo)

        if dest in moo:
            dest_index = moo.index(dest)
            break

        dest -= 1

    # print("Destination:", dest, dest_index)
    # input = input[:cur_cup_index + 1] + input[cur_cup_index + 4: cur_cup_index + dest_index+1] + slice + input[cur_cup_index + dest_index+1:]
    input = moo[:dest_index + 1] + slice + moo[dest_index + 1:]
    cur_cup_index = (input.index(cur_cup) + 1) % len(input)

    # print()
    # print("-" * 20)
    # print()



print("Input:", input)
