"""
Day 5 of Advent of code
"""
from timeit import default_timer as timer

steps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def parse_input(data: str) -> tuple[list[int], dict[str, list[int]]]:
    block_strs = data.split("\n\n")
    maps = {}
    seeds = [int(seed) for seed in block_strs[0].split(": ")[1].split(" ")]
    for block in block_strs[1:]:
        lines = block.split("\n")
        id = lines[0].split(" ")[0]
        maps[id] = [
            [int(val) for val in values.split(" ")] for values in lines[1:]
        ]
        maps[id] = [
            [line[1], line[1]+line[2]-1, line[0], line[0]+line[2]-1] for line in maps[id]
        ]
        maps[id] = sorted(maps[id], key=lambda v: v[0])
        more = []
        if maps[id][0][0] > 0:
            more.append([0, maps[id][0][0]-1, 0, maps[id][0][0]-1])
        for i in range(1,len(maps[id])):
            if maps[id][i][0]-maps[id][i-1][1] > 1:
                span = maps[id][i][0] - maps[id][i-1][1] - 2 # - 2 to take off the start and end
                more.append([maps[id][i-1][1]+1, maps[id][i][0]-1, maps[id][i-1][1]+1, maps[id][i-1][1]+1+span])
        maps[id] = sorted((maps[id]+more), key=lambda v: v[0])

    return (seeds, maps)

# Create a reduced map that takes the ranges of input seeds, and maps
# to the ranges of outputs. We can then find the minimum value of output
# (which is the starting value in the minimum final location range).
# The format of our mapping from input to output will be a list of lists
# where each line is a range:
#    [minimum seed, maximum seed, minimum location, maximum_location]
def reduce_maps(maps, seeds):
    # Convert the seed ranges to our starting map-
    # in_min => out_min, in_max => out_max
    in_out = [[seed[0], seed[1], seed[0], seed[1]] for seed in seeds]
    # Sort in ascending input
    in_out = sorted(in_out, key=lambda v: v[0])

    # iterate over the indexes of our steps, seed-to-soil -> soil-to-fertilizer -> etc.
    for i in range(0, len(steps)):
        # Get the current step, e.g. seed-to-soil
        next_step = steps[i]
        # grab the sorted in/out map for this step.
        in_map = sorted(maps[next_step], key=lambda v:v[0])
        tmp_map = []
        # iterate over our existing global in/out map
        for line in in_out:
            # get the starting and ending output values that the current global map has
            start_val = line[2]
            end_val = line[3]

            # find the index in our current step map that contains this line's start_val
            found = [i for i, val in enumerate(in_map) if val[0]<=start_val and val[1]>=start_val]
            
            # if we found an index, then solve for the new sub-map
            if len(found) > 0:
                found = found[0]
                # iterate and split up the current step's map, and add to our tmp map
                while start_val <= end_val:
                    dist = start_val - line[2]
                    # if we've exceeded the existing current step's map, pass through
                    # the reamining values, then break.
                    if found >= len(in_map):
                        tmp_map.append([line[0]+shift+2, line[1], line[2]+dist+2, line[3]])
                        break
                    shift = start_val - in_map[found][0]
                    found_end = in_map[found][1]
                    end = min(end_val, found_end)
                    range_size = end-start_val
                    # Solve for the proper mapping, and append to tmp_map.
                    tmp_map.append([line[0]+dist, end, in_map[found][2] + shift, in_map[found][2] + shift+range_size])
                    start_val = end + 1
                    found += 1
            else: #if we didnt find the index, just append the line, as input maps to output.
                tmp_map.append(line)
        # at the end of the step, re-sort our new global map by ascending input
        in_out = sorted(tmp_map, key=lambda v: v[0])
    # before returning, sort by the minimum range output. Thus, in_out[0][2] will be our
    # minimum location for the input seeds.
    in_out = sorted(in_out, key=lambda v: v[2])
    return in_out

def lookup(val, step, maps) -> int:
    found = [x for x in maps[step] if x[0] <= val and x[1] >=val]
    if len(found) == 0 :
        return val
    shift = val-found[0][0]
    return found[0][2]+shift

def part1(filename: str) -> int:
    """
    Part 1
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data_str = f.read()

    seeds, maps = parse_input(data_str)
    min_val = 1e99
    for seed in seeds:
        val = seed
        for step in steps:
            val = lookup(val, step, maps)
        min_val = min(min_val, val)

    return min_val


def part2(filename: str) -> int:
    """
    Part 2
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data_str = f.read()

    seeds, maps = parse_input(data_str)
    seeds = [[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0, len(seeds), 2)]
    in_out = reduce_maps(maps, seeds)
    return in_out[0][2]


if __name__ == "__main__":
    print("---- Part 1 ----")
    test = part1("test_data_1.txt")
    print(f" Test:  {test}")
    final = part1("input.txt")
    print(f" Final: {final}")
    print("---- Part 2 ----")
    test = part2("test_data_1.txt")
    print(f" Test:  {test}")
    start = timer()
    final = part2("input.txt")
    end = timer()
    print(f" Final: {final}")
