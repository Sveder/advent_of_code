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

# input = """.#.
# ..#
# ###"""

cycles_count = 6


def step(world):
    size = len(world[0][0])
    new_size = size + 2

    new_world = copy.deepcopy(world)
    # RESIZE PART:
    # Add new planes and empty world to make sure we have enough canvas to draw on:

    new_world.append([[['.'] * size] * size] * size)
    new_world.insert(0, [[['.'] * size] * size] * size)

    for z, cube in enumerate(new_world):
        cube.append([['.'] * size] * size)
        cube.insert(0, [['.'] * size] * size)

        for i, plane in enumerate(cube):
            new_plane = [['.'] * new_size]

            for line in plane:
                new_plane += [['.'] + line + ['.']]

            new_plane += [['.'] * new_size]
            cube[i] = new_plane

    # Now we have enough room to grow, actually grow:
    directions = list(itertools.product((-1, 0, 1), repeat=4))
    directions.remove((0, 0, 0, 0))

    newer_world = copy.deepcopy(new_world)
    for w, cube in enumerate(new_world):
        for z, plane in enumerate(cube):
            for y, line in enumerate(plane):
                for x, cell in enumerate(line):
                    n_count = 0

                    for dz, dy, dx, dw in directions:
                        try:
                            friend = new_world[w + dw][z + dz][y + dy][x + dx]
                            if friend == "#":
                                n_count += 1
                        except IndexError:
                            pass

                    if cell == '.' and n_count == 3:
                        newer_world[w][z][y][x] = '#'

                    elif cell == '#' and n_count not in (2, 3):
                        newer_world[w][z][y][x] = '.'

    return newer_world

def print_world(world):
    for w, cube in enumerate(world):
        for i, z in enumerate(cube):
            print("z=%s" % i, ' w=%s' % w)
            for y in z:
                print("".join(y))

    print()

cur_world = []
for line in input.split('\n'):
    cur_line = [i for i in line]
    cur_world.append(cur_line)

cur_world = [cur_world]
cur_world = [cur_world]

for i in range(cycles_count):
    print("Cycle:", i)
    # print_world(cur_world)
    cur_world = step(cur_world)

alive = 0

for cube in cur_world:
    for plane in cube   :
        for line in plane:
            alive += line.count('#')

print("Alive:", alive)