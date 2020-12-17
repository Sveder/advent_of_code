import copy
import itertools

input = """###..#..
.#######
#####...
#..##.#.
###..##.
##...#..
..#...#.
.#....##"""
#
# input = """.#.
# ..#
# ###"""

W = H = 3
cycles_count = 6


def step(world):
    size = len(world[0])
    new_size = size + 1

    new_world = copy.deepcopy(world)
    # RESIZE PART:
    # Add new planes and empty world to make sure we have enough canvas to draw on:
    new_world.append([['.'] * size] * size)
    new_world.insert(0, [['.'] * size] * size)

    for i, plane in enumerate(new_world):
        new_plane = [['.'] * (new_size + 1)]

        for line in plane:
            new_plane += [['.'] + line + ['.']]

        new_plane += [['.'] * (new_size + 1)]
        new_world[i] = new_plane


    # Now we have enough room to grow, actually grow:
    directions = list(itertools.product((-1, 0, 1), repeat=3))
    directions.remove((0, 0, 0))

    newer_world = copy.deepcopy(new_world)

    for z, plane in enumerate(new_world):
        for y, line in enumerate(plane):
            for x, cell in enumerate(line):
                n_count = 0

                for dz, dy, dx in directions:
                    try:
                        friend = new_world[z + dz][y + dy][x + dx]
                        if friend == "#":
                            n_count += 1
                    except IndexError:
                        pass

                if cell == '.' and n_count == 3:
                    newer_world[z][y][x] = '#'

                elif cell == '#' and n_count not in (2, 3):
                    newer_world[z][y][x] = '.'

    return newer_world

def print_world(world):
    for i, z in enumerate(world):
        print("z=%s" % i)
        for y in z:
            print("".join(y))

    print()

cur_world = []
for line in input.split('\n'):
    cur_line = [i for i in line]
    cur_world.append(cur_line)

cur_world = [cur_world]

for i in range(cycles_count):
    print("Cycle:", i)
    print_world(cur_world)
    W += 1

    cur_world = step(cur_world)


alive = 0

for plane in cur_world:
    for line in plane:
        alive += line.count('#')

print("Alive:", alive)