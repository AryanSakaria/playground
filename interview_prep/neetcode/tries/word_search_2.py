class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False
class Solution:
    def __init__(self):
        self.root = TrieNode('#')
        self.ans = set()
        self.board = None

    def add_word(self, word):
        trav = self.root
        for char_ in word:
            if not char_ in trav.children:
                trav.children[char_] = TrieNode(char_)
            trav = trav.children[char_]
        trav.is_word = True

    def dfs(self,i, j, root, word_so_far):
        if i >= self.m or j >= self.n or i < 0 or j < 0:
            return
        if not self.board[i][j] in root.children:
            return
        current_char = self.board[i][j]
        if root.children[current_char].is_word:
            self.ans.add(word_so_far + current_char)
        self.board[i][j] = '#'
        #do dfs
        self.dfs(i + 1, j, root.children[current_char],word_so_far + current_char)
        self.dfs(i, j+1, root.children[current_char],word_so_far + current_char)
        self.dfs(i - 1, j, root.children[current_char],word_so_far + current_char)
        self.dfs(i, j-1, root.children[current_char],word_so_far + current_char)
        self.board[i][j] = current_char
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.add_word(word)
        
        self.board = board
        self.m, self.n = len(board), len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, self.root,"")
        return list(self.ans)
        