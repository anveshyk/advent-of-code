"""4th puzzle of 2021 AoC - Bingo vs Giant Octopus"""

import sys
import pathlib
from typing import List, Set, Dict, Tuple, Generator, Optional


class Board:
    """Board class with efficient membership check & marking due to Set usage for rows and cols"""

    def __init__(self, size: int = 5):
        self.SIZE = size  # length/dimension of square board
        self.board: List[List[int]] = []  # 2d list of rows (as ints)
        self.won: bool = False
        # self.marked = set()

        # Rows and cols sets - computed once board complete
        self.rows: List[Set[int]] = []
        self.cols: List[Set[int]] = []

    def add_row(self, row: List[str]) -> None:
        # convert to ints
        self.board.append([int(num) for num in row])

        # when last row is added, compute set rows and cols
        if len(self.board) == self.SIZE:
            self._compute_rows()
            self._compute_cols()

    def _compute_rows(self) -> None:
        for row in self.board:
            self.rows.append(set(row))

    def _compute_cols(self) -> None:
        for col_i in range(self.SIZE):
            col = set()
            for row in self.board:
                col.add(row[col_i])
            self.cols.append(col)

    def mark(self, num: int) -> bool:
        """If the num is on the board, remove from row & col
        Returns True if the value is present.
        (Also checks and sets win state boolean for board)"""
        present = False
        for row in self.rows:
            if num in row:
                row.remove(num)
                present = True
                self.won = len(row) == 0 or self.won

        if not present:
            return False

        # Remove same value from its column
        for col in self.cols:
            if num in col:
                col.remove(num)
                self.won = (
                    len(col) == 0 or self.won
                )  # prevent previous won=True getting overwritten
        return True

    def is_won(self) -> bool:
        """Check if board is in a won state, ie any empty rows or cols"""
        return self.won

    def unmarked_sum(self) -> int:
        """Return total sum of all unmarked nums on the baord"""
        total = 0
        for row in self.rows:
            total += sum(row)
        return total

    def __repr__(self):
        repr = "\n"
        for row in self.rows:
            repr += row.__repr__()
            repr += "\n"
        return repr


def parse(input: str) -> Tuple[List, List]:
    """Parse input - return list of drawn numbers and list of board matrices"""
    input_as_lines = input.splitlines()
    drawn_nums: List[int] = [int(num) for num in input_as_lines[0].split(",")]
    boards: List[Board] = []
    curr_board: Board = Board()

    for line in input_as_lines[2:]:
        if line:
            curr_board.add_row(line.split())
        else:
            boards.append(curr_board)
            curr_board = Board()
    boards.append(curr_board)

    # print(drawn_nums, boards)
    return drawn_nums, boards


def get_winning_board_and_num(drawn_nums: List, boards: List) -> Tuple[Optional[Board], Optional[int]]:
    """Part 1 helper function"""
    # check each num in each board, mark if present
    for num in drawn_nums:
        for board in boards:
            marked = board.mark(num)
            if marked and board.is_won():
                return board, num
    return None, None


def part1(data: Tuple[List, List]) -> int:
    """Solve part 1 - find first winning board and calc score with unmarked nums * winning num"""
    drawn, boards = data
    winning_board, final_num = get_winning_board_and_num(drawn, boards)
    # print(final_num, winning_board, winning_board.unmarked_sum())
    score: int = final_num * winning_board.unmarked_sum()
    return score


def get_losing_board_and_num(drawn_nums: List, boards: List) -> Tuple[Board, int]:
    """Part 2 helper function
    Find the losing board, and it's score if it won
    Method: Find winning score for every board, record worst (ie greatest turns to complete) board"""
    worst_board = highest_turn_no = None
    for board in boards:
        for turn_no, num in enumerate(drawn_nums):
            marked = board.mark(num)
            if marked and board.is_won():
                if highest_turn_no is None or turn_no > highest_turn_no:
                    worst_board = board
                    highest_turn_no = turn_no
                break
    # highest_turn_no == index of final drawn num for worst board
    return worst_board, drawn_nums[highest_turn_no]


def part2(data: Tuple[List, List]) -> int:
    """Solve part 2 - find score of the losing/worst board"""
    drawn, boards = data
    worst_board, final_num = get_losing_board_and_num(drawn, boards)
    score: int = final_num * worst_board.unmarked_sum()
    return score


def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input"""
    data1 = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1: int = part1(data1)
    solution2: int = part2(data2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions: Tuple[int, int] = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
