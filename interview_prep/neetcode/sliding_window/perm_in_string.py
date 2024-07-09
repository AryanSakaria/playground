class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count = {}
        count2 = {}
        for s in s1:
            count[s] = 1 + count.get(s, 0)
        for i in range(n2):
            count2[s2[i]] = 1 + count2.get(s2[i],0)
            if i >= n1 - 1:
                check_valid = True
                for s in count:
                    if not s in count2:
                        check_valid = False
                        break
                    if not count[s] == count2[s]:
                        check_valid = False
                        break
                if check_valid:
                    return True
                count2[s2[i + 1 - n1]] -=1
        return False
        