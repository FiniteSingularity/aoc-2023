"""
Day 8 of Advent of code
"""
import math

def parse_file(file) -> tuple[list[int], dict[str, tuple[str, str]]]:
    data = file.readlines()
    directions = data[0].strip()
    directions_list = [0 if d == 'L' else 1 for d in directions]
    nodes: dict[str, tuple[str, str]] = {}
    for node_dat in data[2:]:
        node, l, r = node_dat.strip().replace(' = (', ',').replace(', ', ',').replace(')', '').split(',')
        nodes[node] = (l, r)

    return (directions_list, nodes)


def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    directions, nodes = parse_file(file)
    i = 0
    dc = len(directions)
    current_node = 'AAA'
    while(current_node != 'ZZZ'):
        dir = directions[i % dc]
        current_node = nodes[current_node][dir]
        i+=1
    return i


def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    i = 0
    directions, nodes = parse_file(file)
    dc = len(directions)
    current_nodes = [node for node in nodes if node[-1]=='A']
    cycle_lengths = [0 for node in nodes if node[-1]=='A']
    # Loop until we get the cycle length for all of our starting
    # points.
    while(any([val == 0 for val in cycle_lengths])):
        dir = directions[i % dc]
        current_nodes = [nodes[cn][dir] for cn in current_nodes]
        i+=1
        # Check for any nodes that end in Z, and add cycle length
        # to the proper ghost index if it is currently zero.
        for id, val in enumerate(current_nodes):
            if val[-1] == 'Z' and cycle_lengths[id] == 0:
                cycle_lengths[id]=i
    # Return the least common multiple of all the cycle lengths.
    return math.lcm(*cycle_lengths)


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
