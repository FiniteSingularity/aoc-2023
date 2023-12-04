"""
Day 4 of Advent of code
"""
import re

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    sum: int = 0
    # Strip out line endings and replace multiple spaces with single space,
    # then parse and loop over the cards.
    for line in [re.sub(r'[ ]{2,}', r' ', line.strip()) for line in file.readlines()]:
        # Split the card data into the card numbers, and the winning number strings
        num_dat, win_dat = line.split(": ")[1].split(" | ")
        # Get sets of card numbers and winning numbers
        numbers = set([int(num) for num in num_dat.strip().split(" ")])
        winners = set([int(num) for num in win_dat.strip().split(" ")])
        # Add 2^number of winning cards, which is the count of the intersection
        # between the card numbers and winning numbers
        sum += int(2**(len(numbers.intersection(winners))-1))
    
    return sum


def card_counts(card_winners, i, counts):
    counts[i] += 1
    for j in range(i+1, i+card_winners[i]+1):
        card_counts(card_winners, j, counts)
    return


def part2_recursion(filename: str) -> int:
    """
    Part 2 using Recursion
    """
    file = open(filename, 'r', encoding="utf-8")
    card_winners = []
    # Similar to part1, but assemble a list of how many cards each card wins
    for line in [re.sub(r'[ ]{2,}', r' ', line.strip()) for line in file.readlines()]:
        num_dat, win_dat = line.split(": ")[1].split(" | ")
        numbers = set([int(num) for num in num_dat.strip().split(" ")])
        winners = set([int(num) for num in win_dat.strip().split(" ")])
        card_winners.append(len(numbers.intersection(winners)))
    
    counts = [0 for i in range(len(card_winners))]
    # Solve recursively (slow but fun!)
    for i in range(len(card_winners)):
        card_counts(card_winners, i, counts)
    return sum(counts)


def part2_fast(filename: str) -> int:
    """
    Part 2 using reverse stepping
    """

    file = open(filename, 'r', encoding="utf-8")
    card_winners = []
    # Similar to part1, but assemble a list of how many cards each card wins
    for line in [re.sub(r'[ ]{2,}', r' ', line.strip()) for line in file.readlines()]:
        num_dat, win_dat = line.split(": ")[1].split(" | ")
        numbers = set([int(num) for num in num_dat.strip().split(" ")])
        winners = set([int(num) for num in win_dat.strip().split(" ")])
        card_winners.append(len(numbers.intersection(winners)))

    # Reverse the card_winners list
    card_winners = card_winners[::-1]
    # Initialize the winnings list
    winnings = [0 for i in card_winners]
    
    # Iterate over card_winners, and add the prior number of winning card copy counts
    for i, new_cards in enumerate(card_winners):
        winnings[i] = 1 + sum([addl_cards for addl_cards in winnings[max(0, i-new_cards):i]])
    return sum(winnings)


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 Recursion ----")
    test = part2_recursion("test_data_1.txt")
    print(f" Test:  {test}")
    final = part2_recursion("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 Fast ----")
    test = part2_fast("test_data_1.txt")
    print(f" Test:  {test}")
    final = part2_fast("input.txt")
    print(f" Final: {final}")