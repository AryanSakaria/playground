class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('#')

    def addWord(self, word: str) -> None:
        trav = self.root
        for char_ in word:
            if not char_ in trav.children:
                trav.children[char_] = TrieNode(char_)
            trav = trav.children[char_]
        trav.is_word = True

    def search_helper(self, root, word, l):
        if l == len(word):
            return root.is_word
        if word[l] == '.':
            for child in root.children:
                if self.search_helper(root.children[child], word, l+1):
                    return True
            return False
        if word[l] in root.children:
            return self.search_helper(root.children[word[l]], word, l+1)
        return False
        
    def search(self, word: str) -> bool:
        return self.search_helper(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)