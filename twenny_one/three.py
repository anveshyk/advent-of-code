"""4th puzzle of 2021 AoC - """

import sys
import pathlib
from typing import List, Set, Dict, Tuple, Generator, Optional


def parse(input: str) -> List[str]:
    """Parse input"""
    binary_numbers = input.splitlines()
    return binary_numbers


def get_gamma_binary(data: List[str]) -> str:
    # create initial dict
    zero_count: Dict = {}  # {col index: zero count in col}
    for i in range(len(data[0])):
        zero_count[i] = 0

    # just counting no of 0's
    for binary_str in data:
        for i, bit in enumerate(binary_str):
            if bit == "0":
                zero_count[i] += 1

    # row count - 0 count = 1 count
    no_of_rows: int = len(data)
    gamma_binary: str = ""
    for i in range(len(data[0])):
        most_common_bit: str = "0" if zero_count[i] > no_of_rows / 2 else "1"
        gamma_binary += most_common_bit
    return gamma_binary


def part1(data: List[str]) -> int:
    """Solve part 1 - find power consumption given binary diagnostic report
    power consumption = gamma rate * epsilon rate
    Rates are found by reducing by index/column of report
    gamma binary value = <most common bits in each col>
    epsilon binary value = <least common bits in each col> = inverse bits of gamma = 2^5 - 1 - gamma decimal val"""

    gamma_binary: str = get_gamma_binary(data)

    gamma: int = binary_to_decimal(gamma_binary)  # decimal
    epsilon: int = 2 ** (len(data[0])) - 1 - gamma  # decimal

    # print(gamma_binary, gamma, epsilon, gamma*epsilon)
    return gamma * epsilon


def binary_to_decimal(bin: str) -> int:
    order: int = 1
    total: int = 0
    for bit in bin[::-1]:
        total += order * int(bit)
        order *= 2
    return total


def invert_binary(bin: str) -> str:
    inverted: str = ""
    for bit in bin:
        opposite = "0" if bit == "1" else "1"
        inverted += opposite
    return inverted


def part2(data: List[str]) -> int:
    """Solve part 2 - life support rating = oxy rating * c02 rating
    Example for oxy rating (keeping most common)
    1. Iterate down first col and count most frequent bit.
    2. Only keep numbers that have the most freq bit in that col in their col)
    3. Repeat for each col until 1 number left

    Implementation: to avoid having to iterate again to find the numbers that satisfy
    Make a list of all numbers with 0's there and one with 1's and keep the longest list"""

    oxy_data: List[str] = data.copy()
    for i in range(len(data[0])):
        zeroes: List[str] = []
        ones: List[str] = []
        for binary in oxy_data:
            if binary[i] == "0":
                zeroes.append(binary)
            else:
                ones.append(binary)

        oxy_data: List[str] = zeroes if len(zeroes) > len(ones) else ones
        if len(oxy_data) == 1:
            break

    assert len(oxy_data) == 1
    oxy_binary: str = oxy_data[0]

    co2_data: List[str] = data.copy()
    for i in range(len(data[0])):
        zeroes: List[str] = []
        ones: List[str] = []
        for binary in co2_data:
            if binary[i] == "0":
                zeroes.append(binary)
            else:
                ones.append(binary)

        co2_data: List[str] = zeroes if len(zeroes) <= len(ones) else ones
        if len(co2_data) == 1:
            break

    assert len(co2_data) == 1
    co2_binary: str = co2_data[0]

    oxy_val: int = binary_to_decimal(oxy_binary)
    co2_val: int = binary_to_decimal(co2_binary)

    print(oxy_binary, oxy_val, co2_binary, co2_val)
    return oxy_val * co2_val


def common_prefix_len(str1: str, str2: str) -> int:
    count: int = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            break
        count += 1
    return count


def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1: int = part1(data)
    solution2: int = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Tuple[int, int] = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
