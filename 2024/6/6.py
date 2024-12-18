from copy import deepcopy
import time
data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

data = """.#....#...................#................#......................#.#...............#................#....#...........#..........#
.................................#.....#............#............#.......#...#...##........#..............................#.......
..............#.#............#...............................................##.................#....................#..#.........
..............#.............................#...........................#....#....#........#.................................#..#.
............#.#..#.#...........................#.....................................#..........#............#....................
.#......................................................................#..................................#......#............#.#
...........#.............................#....................#...#.....#........#....##.........................................#
......#..##.......................................................................#............#..................................
........#.......#..........#.......#........#..................#....................#.............#.....................#.........
................#....#.##.........................#........#....#.................#...............................................
.............#........................................#....................#...............#.....#.............#...............#..
..........#.........................#...#.......................#.............................................#......#............
........#................................................#..........#.............#.............#.........#....................#..
....#............#................#.....#.#................#..................#.................#.................................
....#.........................#.............#.....#..................#....#............#...................................#......
...##....................#.............#...............................................#..........................................
.....##.......................#...................#................#..........#.....................#...................#.........
....#....#..................................................#.......................................................#.............
...#........##.........................#.......................#........#...................#...........#...................#.....
.....................##.#...................................................................#.............#.......................
........#..............#...................................................#.....................#...#.......#..#.............#...
..................................................#.......#...............#.............#........#..#.....................#.......
..#..................#...............##..................#.#.........#..........#..............#....................#..#..........
...#..................................................#...........................................#........#......................
#.................................................#..............#...#..........#....................#....................#......#
..#...#....#...........#.................................#......................................#.......................#.....#...
...#...........#..#................................#......#.............#........................##.................#....#....#...
....................#.........#.......................................................................................#...........
............................................................#................#.#..#.....#.....................#...................
.......................................#......#....................................#........................................#.....
...........#.............#...............................#..........#.........#...#.......................................#.......
.............#...............................#.#...................................................#.....#............#...........
.......................................#...#....................#.#..........##.................#...............#............#....
....................#..#....#.............#..............#....#.........................................#.##.....#................
......##..............................................................................................#...........................
....#.......#.............................#..#.........#................................#.........#...............................
..........................................................................#...............................#...........#.#.........
...............#..................................................#.........#.....................#...............#...............
.........#......#............#.........#................................#..............................##.........................
...............#.....................................#............................................#........................#......
..#...........#...........................................#.........................................................#.............
................................#......##..#............................................................................#.........
.........#...........................................#....#..............#......................##....#..#........................
.....#.............#.....#........##......................#...#..................................................#.........#..#.#.
...........................#.........#.......#..........................##...........................#..............#.............
...............................................................................#..#........................#................#.#...
.....#.#.............................................................#.........#...........#..................................#...
.....#....#..#........#....................................#......................................................................
#......................................#..#..............................#..#................#........#...........................
.....................................................................................................#.......#....#.........#.....
....#....#............................................#................................................................#..........
......#.................#.......#..............................................#...................#..............................
...................#.........................................................................................#....................
.............................#................#.#......#...#.......................................#............#............#....
...........................................................#..........#..#.................##.....#..#............................
.....#......................................................#..............................#........................#.............
...............................................#.............#........#.......................................#.......#...........
.............................................................#.............................#...........#.#...................#....
.......#......#......#......................#..................................#^.......................#.........#.......#.......
...........................................................................................................#....................#.
.....#............#.....................#....................#....................................................................
....#...........#................#.....##.............................................................#....................#......
.................................#.#....................#......................#......................#.#.................#.......
..................#......#...#..........#............#................#...#.................................................#.....
...............................................................................................................#...#.........#....
...............#.........#..............................#.......#.......#.......#.................................................
.#........#...#......................................#........#...#.......................................................#..#....
.....#...............................................................#.....#..........#.........#.....................#...........
.........................................................................................................#...#.........#......#...
.....##..................#...#.....#.........#......................................#...............................#.............
..#...............................................................................................#...............................
........#..............................#.#........#.#..#...................................................#.#....................
........................................................#........................#..#.............................................
.....................#.......................#..................................#..........................#....#.................
.........................##.........#.................................#................................#....#.....................
..#........#.......................................................................#.....#........................................
.....#.....................................#.....#....................#...............#...........................................
......................#....................................................................................................#......
...#.........................#......................................................#.......#.......#..#.....................#....
............#...#....................................................#....#......#...............#.......#......................##
.......#.................................................#...#.....................#..................#...........................
.#...................#.....#.#..............................................................................#.....................
..........#...............#......#...........#......................................................#.....#.............#...#....#
.......##.........#.....................................................#....#.........................................#.........#
..##..................#............#..#........................................#..................#..##...........................
..................#....##..............................#.....#...............#.................................................#..
........#..........#...................#.............#...............#..#........#................................................
........#..............................................##....#....................................................................
.........#.#............#.........................#..............#................................#......................#........
........#.#............................#.....#....................................................................#...............
.......................................#......................#...........................#.......................................
..........................##.....................##..#............................................................................
#.............#..............................................................................#...........#........................
......#....#.....................................#........................#.......................................................
#...................#.#.......#.......#.....................#.....#...........................................#...................
...#.......................................#............................................#................#........................
...........#.............................#........................................................................................
...............................................................#.............#..................................................#.
.........#........#....#.#..............................................#.........................................................
.........#....#....#...................#..........#............................................#..##..............................
....#...#.......................#..#....................#...#..........................##..#....#.........................#.......
....#.....##...........................#.#..............#.......................#...#.......................................#.....
......................................................................................#.#..#.....#............##....#....#........
..............#..................................................................##....#.............#............................
................##...#..............#........................#.......................#.#...#......................#...............
...#............................#...#......#.#............#........#......................#........#................#.............
..........#.....................................#.....#...............................................................#.........##
.........#.......#...................#.#.........................................................#................................
...........................#.#............................#...................#.................#.........#.......................
.....#....#.........#................................................................................#...#..................#.....
...............................#....#............................#............................................#.............#.....
......#...............#......#.........................#.#........................................................................
.......................................................................................#...................#.........#.#..#.......
.....#...................................#..................................................................#........#............
...........................................#.......................................#....................#............#...#........
....#............................#..................................#.#....#......................#....#..#.......#...#...........
.#....#................................................#..................#.......##..........................#...#...............
........#...................##...........................................................#...................................#.#..
...#..........#.#....#...................#......#................................................................#................
....#............................#....#......#..#............#..................#........#..........#....#....#........#.#........
................#....#...............#...#.#..............................................#............#................#.........
.......#.....#.#.................#......................................................................#..#......................
.#......................#.................................................#......#..........#......#....................#.........
......#.#............................#............#.......#............#.....#....................................................
.#.............#.........#..................................................#...#...........#..........#............#..#..........
...........#......#...........#............................#.......#......#......#..........#....##..#............#...............
..........................#........#.........................................................#......#........................##...
.................#....#............#...#...........................#....#....#....#...#...........................................
.............#.......................................................#.........#..................................................
....#.................................#...............#.....#....#......##..............#.......................#........#........"""

board_game = []
for i in data.splitlines():
    board_game.append(list(i))

DIRECTIONS_MAP = {
    (-1, 0) : (0, 1),
    (0, 1) : (1, 0),
    (1, 0) : (0, -1),
    (0, -1) : (-1, 0)
}

MAX_STEPS = 48910
MAX_STEPS = 20000


def print_map(board_game, guard):
    for i, line in enumerate(board_game):
        for j, space in enumerate(line):
            if (i, j) == guard:
                print("^", end="")
            else:
                print(space, end="")
        print()
    print("---")

def find_guard_start(board_game):
    for x, line in enumerate(board_game):
        for y, char in enumerate(line):
            if char == "^":
                return (x, y)


def patrol(map, max_steps, guard):
    guard_direction = (-1, 0)
    positions_visited = [(guard, guard_direction)]
    map_len = len(map)
    map_width = len(map[0])
    position_count = 0
    
    while True:
        new_guard = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
        if new_guard[0] < 0 or new_guard[0] >= map_len or new_guard[1] < 0 or new_guard[1] >= map_width:
            return False, positions_visited
        
        while map[new_guard[0]][new_guard[1]] == "#":
            guard_direction = DIRECTIONS_MAP[guard_direction]
            new_guard = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])

        guard = new_guard
        if (guard, guard_direction) in positions_visited:
            return True, positions_visited
        else:
            positions_visited.append((guard, guard_direction))
            position_count += 1

        if position_count > max_steps:
            print("Too many steps!")
            return False, positions_visited
    

loop_count = 0
guard_start = find_guard_start(board_game)
print(len(board_game), len(board_game[0])   )


_, initial_path = patrol(board_game, MAX_STEPS, guard_start)
all_positions = [i[0] for i in initial_path[1:]]
all_positions = list(set(all_positions))

for guard_position in all_positions:
    start_time = time.time()
    space = board_game[guard_position[0]][guard_position[1]]

    if space == ".":
        new_board_game = deepcopy(board_game)
        new_board_game[guard_position[0]][guard_position[1]] = "#"

        looped, _ = patrol(new_board_game, MAX_STEPS, guard_start)
        if looped:
            loop_count += 1
            print("Found loop at", guard_position)

    end_time = time.time()


print("Loop count:", loop_count)
