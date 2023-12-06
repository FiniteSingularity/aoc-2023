"""
Day 6 of Advent of code
"""
import re
import math

def parse_input(file) -> tuple[list[int], list[int]]:
    data_str = file.read()
    times_str, dist_str = data_str.split("\n")
    times = [int(time) for time in re.sub(r'  +', r' ', times_str).split(" ")[1:]]
    distances = [int(dist) for dist in re.sub(r'  +', r' ', dist_str).split(" ")[1:]]
    return (times, distances)

def parse_input_2(file) -> tuple[int, int]:
    data_str = file.read()
    times_str, dist_str = data_str.split("\n")
    time = int("".join([time for time in re.sub(r'  +', r' ', times_str).split(" ")[1:]]))
    distance = int("".join([dist for dist in re.sub(r'  +', r' ', dist_str).split(" ")[1:]]))
    return(time, distance)

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    times, distances = parse_input(file)
    prod = 1
    for t, d in zip(times, distances):
        # given a total time: t, distance: d and hold time: h
        # we can make a quadratic equation of the relationship:
        # -1.0*h^2 + t*h = d, or -1.0*h^2 + t*h - d = 0

        # solve for the two hold times on the quadratic curve that 
        # equal the record time.  Shift by a small epsilon for
        # cases where the solution is an integer.
        v1 = (-t + math.sqrt(t**2 - 4*d)) / -2 + 1.e-10
        v2 = (-t - math.sqrt(t**2 - 4*d)) / -2 - 1.e-10
        win_count = math.floor(v2)-math.ceil(v1)+1
        prod *= win_count
    return prod


def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    t, d = parse_input_2(file)
    # given a total time: t, distance: d and hold time: h
    # we can make a quadratic equation of the relationship:
    # -1.0*h^2 + t*h = d, or -1.0*h^2 + t*h - d = 0

    # solve for the two points on the quadratic curve that 
    # equal the record time.  Shift by a small epsilon for
    # cases where the solution is an integer.
    v1 = (-t + math.sqrt(t**2 - 4*d)) / -2 + 1.e-10
    v2 = (-t - math.sqrt(t**2 - 4*d)) / -2 - 1.e-10
    return math.floor(v2)-math.ceil(v1)+1


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
