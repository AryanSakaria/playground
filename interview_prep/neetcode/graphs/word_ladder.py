class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        
        adj_list = collections.defaultdict(list)
        word_len = len(beginWord)
        
        wordList.append(beginWord)
        for word in wordList:
            for j in range(word_len):
                pattern = word[:j] + '*' + word[j+1:]
                adj_list[pattern].append(word)
        
        q = deque()
        visit = set()
        q.append(beginWord)
        visit.add(beginWord)
        level = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for j in range(word_len):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei in visit:
                            continue
                        visit.add(nei)
                        q.append(nei)

            level += 1
        return 0