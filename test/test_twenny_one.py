"""PyTest AoC Testing template
- inspired by https://realpython.com/python-advent-of-code

Run with: python -m pytest"""

import pathlib
import pytest
from twenny_one import four as solution

APP_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = APP_DIR.joinpath("twenny_one", "input")


# DAY 4

@pytest.fixture
def parse_four():
    puzzle_input = (INPUT_DIR / "04_test.txt").read_text().strip()
    return solution.parse(puzzle_input)


def test_parse(parse_four):
    """Test that input is parsed properly"""
    drawn, _ = parse_four
    assert drawn == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def test_part1_example1(parse_four):
    """Test Part 1"""
    assert solution.part1(parse_four) == 4512


#@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(parse_four):
    """Test Part 2"""
    assert solution.part2(parse_four) == 1924


