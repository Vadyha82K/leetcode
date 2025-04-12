# 38. Valid Sudoku
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, elem in enumerate(row):
                if elem == ".":
                    continue

                idx_boxes = (idx_row // 3, idx_col // 3)

                if (
                    elem in cols[idx_col]
                    or elem in rows[idx_row]
                    or elem in boxes[idx_boxes]
                ):
                    return False

                cols[idx_col].add(elem)
                rows[idx_row].add(elem)
                boxes[idx_boxes].add(elem)
        return True