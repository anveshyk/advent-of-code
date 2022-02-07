"""1st puzzle of 2021 AoC - Sonar Sweep"""

import sys
import pathlib


def parse(input):
    """Parse input"""
    # create list of depths, 1 depth per line
    return (int(num) for num in input.split())


def part1(depths):
    """Solve part 1 - no of subsequent depth increases"""
    prev_depth = None
    no_of_increases = 0
    for depth in depths:
        if prev_depth and depth > prev_depth:
            no_of_increases += 1
        prev_depth = depth
    return no_of_increases


def part2(depths):
    """Solve part 2 - sliding window of length 3, no of subsequent bigger window sums"""
    from collections import deque

    window = deque()  # queue containing 3 elements = sliding window
    no_of_increases = 0
    prev_sum = 0
    for depth in depths:
        window.append(depth)
        # create initial sliding window sum
        if len(window) <= 3:
            prev_sum += depth
            # print(prev_sum)
        # create new sum & check for increase
        else:
            curr_sum = prev_sum - window.popleft() + depth
            if curr_sum > prev_sum:
                no_of_increases += 1
            prev_sum = curr_sum
    return no_of_increases


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data1 = parse(puzzle_input)
    data2 = parse(puzzle_input)
    # print(data)
    solution1 = part1(data1)
    solution2 = part2(data2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
