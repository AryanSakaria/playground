class Solution:
    def isValid(self, s: str) -> bool:
        l, n = 0, len(s)
        stack = []
        map_dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        while l < n:
            if s[l] in ['(','{','[']:
                stack.append(s[l])
                l+=1
            elif not stack:
                return False
            else:
                if s[l] != map_dict[stack[-1]]:
                    return False
                else:
                    stack.pop()
                    l+=1
        return True if not stack else False