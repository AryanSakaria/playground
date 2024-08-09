class Solution:
    def bin_search(self, target):
        l, r = 0, len(self.lis) - 1
        while l < r:
            mid = l + r
            mid = mid // 2
            if self.lis[mid] == target:
                return mid
            if self.lis[mid] < target:
                l = mid + 1
            else:
                r = mid 
        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.lis = [nums[0]]

        for num in nums[1:]:
            if num > self.lis[-1]:
                # print("case 1", num)
                self.lis.append(num)
            else:
                
                l_ = self.bin_search(num)
                # if num == 7:
                #     print("case 2", l_, " ", num)
                self.lis[l_] = num
            # print(self.lis)
        return len(self.lis)

        