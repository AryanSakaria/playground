class Solution:
    def __init__(self):
        self.cache = {}
        self.directory = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if digits in self.cache:
            return self.cache[digits]

        if len(digits) == 0:
            self.cache[digits] = []
            return []
        if len(digits) == 1:
            self.cache[digits] = [*self.directory[digits]] 
            return [*self.directory[digits]] 
        ans = []
        
        single_list = self.letterCombinations(digits[0])
        multilist = self.letterCombinations(digits[1:])
        for elem in single_list:
            for elem_multi in multilist:
                ans.append(elem + elem_multi)
        self.cache[digits] = ans.copy()
        return ans
        