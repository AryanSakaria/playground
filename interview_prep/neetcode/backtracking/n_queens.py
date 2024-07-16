class Solution:
    def dfs(self, row):
        if row == len(self.board):
            self.ans.append(["".join(k) for k in self.board])
        for i in range(self.n):
            if i in self.col or (row + i) in self.posDiag or (row - i) in self.negDiag:
                continue
            self.board[row][i] = 'Q'
            self.col.add(i)
            self.posDiag.add(row + i)
            self.negDiag.add(row - i)
            self.dfs(row+1)
            self.board[row][i] = '.'
            self.col.remove(i)
            self.posDiag.remove(row + i)
            self.negDiag.remove(row - i)
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.n = n
        self.ans = []
        self.col = set()
        self.posDiag = set()
        self.negDiag = set()

        self.dfs(0)
        return self.ans
        