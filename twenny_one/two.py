"""2nd puzzle of 2021 AoC - submarine movement"""

import sys
import pathlib


def parse(input):
    """Parse input, each row has (direction, distance)"""
    return ((row.split()[0], int(row.split()[1])) for row in input.splitlines())


def part1(data):
    """Solve part 1 - count up horizontal and vertical distance moved"""
    hor_pos = 0  # horizontal position
    depth = 0
    for dir, dist in data:
        if dir == "forward":
            hor_pos += dist
        elif dir == "down":
            depth += dist
        elif dir == "up":
            depth -= dist
        else:
            print("ERROR")
    return hor_pos * depth


def part2(data):
    """Solve part 1 - count up horizontal and vertical distance moved"""
    hor_pos = depth = aim = 0
    for dir, dist in data:
        if dir == "forward":
            hor_pos += dist
            depth += aim * dist
        elif dir == "down":
            aim += dist
        elif dir == "up":
            aim -= dist
        else:
            print("ERROR")
    return hor_pos * depth


def solve(input):
    """Solve the puzzle for the given input"""
    data1 = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1 = part1(data1)
    solution2 = part2(data2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
