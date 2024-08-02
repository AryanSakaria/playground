class Solution:
    def dfs(self, i, j, board):
        if i < 0 or i >=self.m:
            return
        if j < 0 or j >= self.n:
            return 
        if board[i][j]!='O':
            return
        board[i][j] = 'T'
        self.dfs(i+1, j, board)
        self.dfs(i-1, j, board)
        self.dfs(i  ,j+1, board)
        self.dfs(i  ,j-1, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if i!=0 and j!=0 and i!=self.m-1 and j!=self.n-1:
                    continue
                if board[i][j] == 'O':
                    self.dfs(i, j, board)
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return
        
        