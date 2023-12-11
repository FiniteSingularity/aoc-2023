"""
Day 10 of Advent of code
"""
import math

# coordinate increment for different directional moves
right = ( 0, 1)
left =  ( 0,-1)
up =    (-1, 0)
down =  ( 1, 0)

# defines each pipe type, and depending on the incoming move 
# (incoming move up, down, left, right), the increment of the
# current position (up, down, left, right)
pipe_types = {
    '-': {left: left, right: right},
    '|': {down: down,  up: up},
    'F': {up: right, left: down},
    '7': {up: left, right: down},
    'L': {down: right, left: up},
    'J': {down: left, right: up}
}

def parse_file(file) -> list[list[str]]:
    return [list(line.strip()) for line in file.readlines()]

def find_start(pipe_map: list[list[str]]) -> tuple[int, int]:
    row = next((i for i,line in enumerate(pipe_map) if 'S' in line))
    col = pipe_map[row].index('S')
    return (row, col)


def start_direction(start: tuple[int, int], pipe_map: list[list[str]]):
    for dir in [left, right, up, down]:
        index = (start[0]+dir[0], start[1]+dir[1])
        cell = pipe_map[index[0]][index[1]]
        if cell == '.':
            continue
        if dir in pipe_types[cell].keys():
            return dir
    return (-10, -10)

def walk_path(pipe_map):
    loc = find_start(pipe_map)
    direction = start_direction(loc, pipe_map)
    path = []
    current = '.'
    while True:
        loc = (loc[0]+direction[0], loc[1]+direction[1])
        current = pipe_map[loc[0]][loc[1]]
        if current == 'S':
            break
        path.append(current)
        direction = pipe_types[current][direction]

    return path
    
def point_det(pt1: tuple[int, int], pt2: tuple[int, int]):
    return pt1[0]*pt2[1] - pt1[1]*pt2[0]

def calculate_enclosed(pipe_map):
    loc = find_start(pipe_map)
    prior_loc = tuple(loc)
    direction = start_direction(loc, pipe_map)
    path = []
    current = '.'
    area = 0
    boundary_pts = 0
    # Use the Shoelace formula to calculate the area of the polygon
    # Polygon area is half the sum of the determinant of all edge
    # vertices.  E.g.- for edge with P1, P2, take determinant:
    # | p1x p2x |
    # | p1y p2y |
    # The sum of all the determinates will be 2A
    while True:
        loc = (loc[0]+direction[0], loc[1]+direction[1])
        current = pipe_map[loc[0]][loc[1]]
        if current != '-' and current != '|':
            area += point_det(prior_loc, loc)
            prior_loc = tuple(loc)
        boundary_pts += 1 # keep track of number of integer boundary points
                          # for Picks theorem calulation below
        if current == 'S':
            break
        direction = pipe_types[current][direction]
    area /= 2
    area = abs(area)
    
    # Since we know all vertices are integer points, 
    # we can use Pick's theorem to calcuate the number
    # of internal integer points:
    # A = i + b/2 -1
    # where i is the number of internal points, and b
    # is the number of integer boundary points.
    enclosed = int(area - boundary_pts/2 + 1)

    return enclosed

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    pipe_map = parse_file(file)
    path = walk_path(pipe_map)
    return math.ceil(len(path)/2)

def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    pipe_map = parse_file(file)
    return calculate_enclosed(pipe_map)


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 ----")
    test = part2("test_data_2.txt")
    print(f" Test:  {test}")
    final = part2("input.txt")
    print(f" Final: {final}")
