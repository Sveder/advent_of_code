from input import input


SIZE = 10

class TileArrangement:
    def __init__(self, tile, arr_text):
        self.tile = tile
        self.arr_text = arr_text.strip()
        self.arr_list = arr_text.strip().split('\n')

        self.neighbours = {
            "up": None,
            "down": None,
            "left": None,
            "right": None,
        }

class Tile:
    def __init__(self, name, original_text):
        self.name = name
        self.original_text = original_text.strip()
        self.original_list = original_text.strip().split('\n')

        self.possible_arr = []

        self.aligned_neighbours = {
            "up": None,
            "down": None,
            "left": None,
            "right": None,
        }

        self.final_arr = None
        self.is_aligned = False
        self.was_scanned = False

    @staticmethod
    def get_left_side(text):
        r = ""
        for i in text:
            r += i[0]

        return r

    @staticmethod
    def get_right_side(text):
        r = ""
        for i in text:
            r += i[-1]

        return r

    def generate_possibilities(self):
        original = self.original_text
        results = [original]

        rev = ""
        for i in original.split("\n"):
            rev += i[::-1] + "\n"

        results.append(rev)


        for i in [original, rev]:
            upside_down = "\n".join(i.split("\n")[::-1])
            results.append(upside_down)


            clock_wise = "\n".join([
                i[::11][::-1],
                i[1::11][::-1],
                i[2::11][::-1],
                i[3::11][::-1],
                i[4::11][::-1],
                i[5::11][::-1],
                i[6::11][::-1],
                i[7::11][::-1],
                i[8::11][::-1],
                i[9::11][::-1],
            ])

            counter = "\n".join(clock_wise.split("\n")[::-1])

            results.append(clock_wise)
            results.append(counter)

            clock_wise = "\n".join([
                i[::11],
                i[1::11],
                i[2::11],
                i[3::11],
                i[4::11],
                i[5::11],
                i[6::11],
                i[7::11],
                i[8::11],
                i[9::11],
            ])
            counter = "\n".join(clock_wise.split("\n")[::-1])

            results.append(clock_wise)
            results.append(counter)

        for i in list(set(results)):
            self.possible_arr.append(TileArrangement(self, i))

    def determine_relationship(self, candidate):
        for i, my in enumerate(self.possible_arr):
            for j, their in enumerate(candidate.possible_arr):
                if '' in my.arr_list or '' in their.arr_list:
                    import pdb;pdb.set_trace()

                # Is above us?
                if my.arr_list[0] == their.arr_list[-1]:
                    my.neighbours['up'] = their
                    their.neighbours['down'] = my

                # Check whether it is on the bottom:
                if my.arr_list[-1] == their.arr_list[0]:
                    my.neighbours['down'] = their
                    their.neighbours['up'] = my

                # Check whether it is on the left:
                if Tile.get_left_side(my.arr_list) == Tile.get_right_side(their.arr_list):
                    my.neighbours['left'] = their
                    their.neighbours['right'] = my

                # Check whether it is on the right:
                if Tile.get_right_side(my.arr_list) == Tile.get_left_side(their.arr_list):
                    my.neighbours['right'] = their
                    their.neighbours['left'] = my

        return None



def print_board(board):
    for line in board:
        cur_row = ""

        for i, tile in enumerate(line):
            cur_row += str(tile.name) + " " * 11

        cur_row += "\n"

        for i in range(10):
            for t in line:
                cur_row += t.final_arr.arr_list[i] + " " * 5

            cur_row += "\n"

        print(cur_row)


tiles = input.split("\n\n")
tile_dict = {}

for t in tiles:
    tile_number, tile_text = t.split('\n', 1)
    tile_obj = Tile(int(tile_number[4:9]), tile_text)
    tile_dict[int(tile_number[4:9])] = tile_obj
    tile_obj.generate_possibilities()



square = []
square_size = int(len(tile_dict) ** 0.5)
for i in range(square_size):
    square.append([None] * square_size)

#### TEST print board - Randomly put everything into a square:
# for i, j in enumerate(tile_dict.values()):
#     square[i // 3][i % 3] = j
#     j.final_arr = j.possible_arr[0]
#
# print_board(square)
#


for tile_name, tile_obj in tile_dict.items():
    for can_name, can_obj in tile_dict.items():
        if can_obj.was_scanned:
            continue

        if can_obj == tile_obj:
            continue

        relationship = tile_obj.determine_relationship(can_obj)

    tile_obj.was_scanned = True

# ttt = tile_dict[1951]
#
# for i in ttt.possible_arr:
#     for k, v  in i.neighbours.items():
#         if  v != None:
#             print(k, '->', v.tile.name)
#
#     print('-------------')

#
# find top left:
top_left =  None
possible_corners = []

for tile_obj in tile_dict.values():
    for can in tile_obj.possible_arr:
        if can.neighbours['down'] != None and can.neighbours['left'] != None and can.neighbours['right'] == None and can.neighbours['up'] == None:
            print("Top left:", can.neighbours, tile_obj.name)
            possible_corners.append(can.tile.name)

corners = 1

for i in set(possible_corners):
    corners *= i

print("Corners:", corners)
