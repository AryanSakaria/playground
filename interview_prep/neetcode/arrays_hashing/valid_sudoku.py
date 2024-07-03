class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict, cols_dict, sq_dict = {}, {}, {}
        for i in range(9):
            rows_dict[i] = set()
            cols_dict[i] = set()
            sq_dict[i] = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val!='.':
                    if val in rows_dict[i]:
                        return False
                    else:
                        rows_dict[i].add(val)
                    if val in cols_dict[j]:
                        return False
                    else:
                        cols_dict[j].add(val)
                    sq_idx = int(i//3) * 3 + j//3
                    if val in sq_dict[sq_idx]:
                        return False
                    else:
                        sq_dict[sq_idx].add(val)
        return True