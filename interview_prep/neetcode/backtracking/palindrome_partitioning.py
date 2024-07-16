class Solution:
    def __init__(self):
        self.cache = {}
        #Adding memoization

    def check_palindrome(self, str_s):
        n = len(str_s)
        for i in range(n//2):
            if not str_s[i] == str_s[n - 1 - i]:
                return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        if s in self.cache:
            return self.cache[s]

        if len(s) < 1:
            self.cache[""] = []
            return []
        if len(s) == 1:
            self.cache[s] = [[s]]
            return [[s]]
        ans = []
        if self.check_palindrome(s):
            ans.append([s])
        for i in range(len(s)-1):
            current_partition = s[0:i+1]
            if self.check_palindrome(current_partition): 
                partition_lists = self.partition(s[i+1:])
                for a in partition_lists:
                    ans.append([current_partition] + a)
        self.cache[s] = ans.copy()
        return ans
