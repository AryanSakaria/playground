class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end_word = False
class Trie:

    def __init__(self):
        self.root = TrieNode('#')
        
    def insert(self, word: str) -> None:
        trav = self.root
        for char_ in word:
            if not char_ in trav.children:
                trav.children[char_] = TrieNode(char_)
            trav = trav.children[char_]
        trav.end_word = True

    def search(self, word: str) -> bool:
        trav = self.root
        for char_ in word:
            if not char_ in trav.children:
                return False
            trav = trav.children[char_]
        return trav.end_word
        

    def startsWith(self, prefix: str) -> bool:
        trav = self.root
        for char_ in prefix:
            if not char_ in trav.children:
                return False
            trav = trav.children[char_]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)