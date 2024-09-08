class Solution:
    def checkValidString(self, s: str) -> bool:
        maxDiff, minDiff = 0, 0
        c = s
        for s in c:
            if s == '(':
                maxDiff+=1 
                minDiff+=1
            if s == ')':
                minDiff -= 1
                maxDiff -= 1
            if s == '*':
                minDiff -= 1
                maxDiff += 1
            if maxDiff < 0:
                return False
            minDiff = max(0, minDiff)
        return minDiff == 0