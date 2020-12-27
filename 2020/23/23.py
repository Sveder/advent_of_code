import copy

num_to_node = {}

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    @staticmethod
    def from_list(l):
        global num_to_node

        root = last = LinkedList(l[0], None)
        num_to_node[root.value] = root

        for i in l[1:]:
            cur = LinkedList(i, last)
            last.next = cur
            last = cur
            num_to_node[i] = cur

        last.next = root

        return root

    def __str__(self):
        l = [self.value]
        cur = self.next
        while cur != self:
            l.append(cur.value)
            cur = cur.next

        return 'LL:' + ','.join([str(i) for i in l])

input = "253149867"
# input = "389125467"

input = [int(i) for i in input] + list(range(10, 1000000+1))
max_input = max(input)

moves = 10
moves = 100
moves = 10000000

ll_cur = LinkedList.from_list(input)

for i in range(moves):
    # print('Cups:', ll_cur)
    cur_cup = ll_cur.value

    slice_start = ll_cur.next
    ll_cur.next = slice_start.next.next.next
    sliced_values = [slice_start.value, slice_start.next.value, slice_start.next.next.value]

    if i % 1000 == 0:
        print("Move:", i +1)

    # print('Cups:', ll_cur)
    # print('pick ip:', sliced_values)

    dest = cur_cup - 1
    dest_index = ll_cur.next

    while True:
        if dest == 0:
            dest = max_input

        if dest not in sliced_values:
            dest_index = num_to_node[dest]
            break

        dest -= 1

    # print("Destination:", dest, dest_index.value)
    # input = input[:cur_cup_index + 1] + input[cur_cup_index + 4: cur_cup_index + dest_index+1] + slice + input[cur_cup_index + dest_index+1:]
    # input = moo[:dest_index + 1] + slice + moo[dest_index + 1:]
    # cur_cup_index = (input.index(cur_cup) + 1) % len(input)

    ll_cur = ll_cur.next
    slice_start.next.next.next = dest_index.next
    dest_index.next = slice_start


    # print()
    # print("-" * 20)
    # print()



print("Mul:", num_to_node[1].next.value * num_to_node[1].next.next.value)
