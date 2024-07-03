class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupl_set = set()
        for i in nums:
            if i in dupl_set:
                return True
            else:
                dupl_set.add(i)
        return False
