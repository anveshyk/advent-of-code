"""Nth puzzle of 2021 AoC
Template inspired by https://realpython.com/python-advent-of-code/#puzzling-in-programming"""

import sys
import pathlib
from typing import List, Set, Dict, Tuple, Generator, Optional


def parse(input: str) -> List[int]:
    """Parse input"""
    pass


def part1(data: List[int]) -> int:
    """Solve part 1"""
    pass


def part2(data: List[int]) -> int:
    """Solve part 2"""
    pass


def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input"""
    data: List[str] = parse(puzzle_input)
    solution1: int = part1(data)
    solution2: int = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Tuple[int, int] = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
