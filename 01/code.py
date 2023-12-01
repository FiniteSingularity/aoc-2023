"""
Day 1 of Advent of code
"""
import re

number_dict ={
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# Word to number helper function
def w2n(value: str) -> int:
    if value.isnumeric():
        return int(value)
    return number_dict[value]

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()

    total: int = 0
    for line in lines:
        # Search for first numeric digit in string
        first: int = int(re.search(r'\d', line).group())
        # Search reverse string for last digit in string
        last: int = int(re.search(r'\d', line[::-1]).group())
        total += first*10 + last
    return total


def part2(filename: str) -> int:
    """
    Part 2
    """

    file = open(filename, 'r', encoding="utf-8")
    lines: list[str] = file.readlines()
    # Pattern to match a number word
    pattern: str = 'one|two|three|four|five|six|seven|eight|nine'
    # reverse the pattern so that we can search backwards from end
    reverse_pattern: str = pattern[::-1]
    total: int = 0
    for line in [l.strip() for l in lines]:
        # Find the first digit
        first = re.search(rf'(\d|{pattern})', line)
        # Find the last digit by searching for reversed pattern
        # on the reversed string
        last = re.search(rf'(\d|{reverse_pattern})', line[::-1])
        # Update running total
        total += w2n(first.group())*10 + w2n(last.group()[::-1])
    return total


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