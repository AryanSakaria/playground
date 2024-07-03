class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_ = {}
        for num in nums:
            if not num in bucket_:
                bucket_[num] = 0
            bucket_[num]+=1
        flipped_bucket = sorted([(bucket_[key],key) for key in bucket_], reverse=True)
        count = 0
        ans = []
        while count < k:
            ans.append(flipped_bucket[count][1])
            count += 1
        return ans
