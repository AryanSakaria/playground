class Solution:
    # @cache
    # def dfs_i(self, i1, i2):
    #     i3 = i1 + i2
    #     if i3 >= len(self.s3) and i2 >= len(self.s2) and i1 >= len(self.s2):
    #         return True
        
    #     if i1 >= len(self.s1):
    #         return self.s2[i2:] == self.s3[i3:]

    #     if i2 >= len(self.s2):
    #         return self.s1[i1:] == self.s3[i3:]
        

    #     # print(self.s1[i1:], self.s2[i2:], self.s3[i3:])
    #     l = i1
    #     found = False
    #     while l < len(self.s1) and i2 + l < len(self.s3) and self.s1[l] == self.s3[i2 + l]:
    #         found = found or self.dfs_i(l+1, i2)
    #         l += 1

    #     l = i2
    #     while l < len(self.s2) and i1 + l < len(self.s3) and self.s2[l] == self.s3[i1 + l]:
    #         found = found or self.dfs_i(i1, l+1)
    #         l += 1
    #     return found
        
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s1) + len(s2) > len(s3):
        #     return False
        # s1, s2 = sorted([s1,s2] ,key = lambda x: len(x))
        # self.s1, self.s2, self.s3 = s1, s2, s3
        # return self.dfs_i(0, 0)
        # return self.dfs(s1, s2, s3)
        if len(s1) + len(s2) != len(s3):
            return False
        DP = [[False for _ in range(len(s2)+1)] for _ in range(len(s1) + 1)]
        DP[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and DP[i+1][j]:
                    DP[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and DP[i][j+1]:
                    DP[i][j] = True
        return DP[0][0]
                

        