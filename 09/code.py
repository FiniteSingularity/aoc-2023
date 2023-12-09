"""
Day 9 of Advent of code
"""
import math

def parse_file(file) -> tuple[list[int], dict[str, tuple[str, str]]]:
    return [[int(val) for val in line.split(" ")] for line in file.readlines()]


def downscale(vals, index) -> list[int]:
    start_vals = [vals[index]]
    diff = [v for v in vals]
    while(not all(v == 0 for v in diff)):
        diff = [y-x for y,x in zip(diff[1:], diff[0:-1])]
        start_vals.append(diff[index])
    return start_vals


def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    lines = parse_file(file)
    total = 0
    for line in lines:
        values = downscale(line, -1)
        diff = 0
        for val in values:
            diff += val
        total += diff
    return total

def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    lines = parse_file(file)
    total = 0
    for line in lines:
        values = downscale(line, 0)[:-1][::-1]
        diff = 0
        for val in values:
            diff = val - diff
        total += diff
    return total


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 ----")
    test = part2("test_data_1.txt")
    print(f" Test:  {test}")
    final = part2("input.txt")
    print(f" Final: {final}")
