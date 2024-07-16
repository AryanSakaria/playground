
class Solution:
    def dfs(self, word_i, i, j):
        if word_i == len(self.word):
            self.found = True
            return
        if i >= self.m or j >= self.n or i < 0 or j < 0:
            return
        
        if self.word[word_i] != self.board[i][j]:
            return
        
        cur_char = self.board[i][j]
        self.board[i][j] = '#'
        self.dfs(word_i + 1, i+1, j)
        self.dfs(word_i + 1, i, j+1)
        self.dfs(word_i + 1, i-1, j)
        self.dfs(word_i + 1, i, j-1)
        self.board[i][j] = cur_char

        return
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.found = False
        self.word = word
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(0, i, j)
        return self.foundW