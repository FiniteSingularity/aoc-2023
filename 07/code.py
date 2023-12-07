"""
Day 7 of Advent of code
"""
# Relative strength of each card used for
# lexicographical scoring of the hand.
strength = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    '0': 0
}

def parse_file(file) -> list[list[str, int, int]]:
    hands = [[line.split(" ")[0], 0, int(line.split(" ")[1])] for line in file.readlines()]
    return hands

# Here we parse the card, but replace 'J' with '0' to represent Jokers, so
# that we can reuse the scoring algorithm.
def parse_file_jokers(file) -> list[list[str, int, int]]:
    hands = [[line.split(" ")[0].replace('J', '0'), 0, int(line.split(" ")[1])] for line in file.readlines()]
    return hands

def score_hands(hands: list[list[str, int, int]]):
    for hand in hands:
        # Remove Jokers then Count the number of each character in the hand, 
        # and sort in descending order. So 'TT888' would return [3, 2], '12305'
        # would return [1,1] (0 is replaces J for jokers in part 2 when parsed)
        # Also we add [0, 0] for the edge case of 5 of a kind or 5 of a kind for
        # jokers
        res = sorted([hand[0].count(i) for i in set(hand[0].replace('0', ''))]+[0, 0], reverse=True)[0:2]
        
        # Now get the number of jokers in the hand
        jokers = hand[0].count('0')

        # Best score with jokers will just be the highest number of a single card
        # plus the number of jokers
        res[0]+=jokers

        # Now we do a lexicographical score for the order of the cards in the hand.
        # Because there are 14 possible values for a card, we need to multiply
        # the reverse card index by a power of 100.
        order_strength = 0
        for i, char in enumerate(hand[0][::-1]):
            order_strength += 100**i*strength[char]

        # Finally, score the hand based on the descending number of matched cards,
        # then add on the lexicographical score of the card. The huge numbers are 
        # due to the lexicographical score having max values of 100^5
        hand[1] = res[0]*1e12+res[1]*1e11+order_strength
    hands.sort(key=lambda v: v[1])

def part1(filename: str) -> int:
    """
    Part 1
    """
    file = open(filename, 'r', encoding="utf-8")
    hands = parse_file(file)
    score_hands(hands)
    total = 0
    for i, hand in enumerate(hands):
        total += (i+1)*hand[2]
    return total


def part2(filename: str) -> int:
    """
    Part 2
    """
    file = open(filename, 'r', encoding="utf-8")
    hands = parse_file_jokers(file)
    score_hands(hands)
    total = 0
    for i, hand in enumerate(hands):
        total += (i+1)*hand[2]
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
