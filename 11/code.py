"""
Day 11 of Advent of code
"""
import re

def parse_file(file, expansion: int) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    data = [line.strip() for line in file.readlines()]
    galaxies: list[tuple[int, int]] = []
    double_rows: list[int] = []
    for row, line in enumerate(data):
        if not '#' in line:
            double_rows.append(row)
        else:
            galaxies += [(row, m.start(0)) for m in re.finditer(r'(#)', line)]
    double_cols = [col for col, line in enumerate(list(map(list, zip(*[list(line) for line in data])))) if not '#' in line]
    row_indices = [0]
    col_indices = [0]
    for r in range(1, len(data)):
        increment = expansion if r-1 in double_rows else 1
        row_indices.append(row_indices[r-1]+increment)
    for c in range(1, len(data[0])):
        increment = expansion if c-1 in double_cols else 1
        col_indices.append(col_indices[c-1]+increment)
    return (galaxies, row_indices, col_indices)

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    galaxies, rows, cols = parse_file(file, 1)
    steps: int = 0
    for g1i, g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[g1i+1:]:
            steps+= abs(rows[g1[0]]-rows[g2[0]]) + abs(cols[g1[1]]-cols[g2[1]])
    return steps

def part2(filename: str, expansion: int) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    galaxies, rows, cols = parse_file(file, expansion)
    steps: int = 0
    for g1i, g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[g1i+1:]:
            steps+= abs(rows[g1[0]]-rows[g2[0]]) + abs(cols[g1[1]]-cols[g2[1]])
    return steps


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 ----")
    test = part2("test_data_1.txt", 10)
    print(f" Test 1:  {test}")
    test = part2("test_data_1.txt", 100)
    print(f" Test 2:  {test}")
    final = part2("input.txt", 1000000)
    print(f" Final: {final}")
