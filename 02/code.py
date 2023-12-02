"""
Day 2 of Advent of code
"""
import math

# Returns the maximum number of each color drawn for all pulls in 
# a game line.\
def parse_line(line: str) -> tuple[int, dict[str, int]]:
    line=line.strip()
    game: dict[str, int] = {
        'blue': 0,
        'red': 0,
        'green': 0
    }
    game_pulls: list[str] = line.split(": ")[1].split("; ")
    game_id: int = int(line.split(": ")[0].split(" ")[1])
    for pull in game_pulls:
        res: dict[str, int] = {cube.split(" ")[1]: int(cube.split(" ")[0]) for cube in pull.split(", ")}
        for color, count in res.items():
            game[color]=max(game[color], count)

    return (game_id, game)

def part1(filename: str) -> int:
    """
    Part 1
    """
    max_valid = {
        'red': 12, 'green': 13, 'blue': 14
    }
    file = open(filename, 'r', encoding="utf-8")
    lines: list[str] = file.readlines()
    id_sum: int = 0
    for line in lines:
        game_id, results = parse_line(line)
        if all([results[x] <= max_valid[x] for x in results]):
            id_sum += game_id
    return id_sum


def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    lines: list[str] = file.readlines()
    sum: int = 0
    for line in lines:
        _, results = parse_line(line)
        sum += math.prod(results.values())
    return sum


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