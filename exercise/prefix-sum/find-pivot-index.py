from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        suffix_sum = []

        gain = 0
        for v in nums:
            gain += v
            prefix_sum.append(gain)

        gain = 0
        for v in nums[::-1]:
            gain += v
            suffix_sum.append(gain)
        
        suffix_sum = suffix_sum[::-1]

        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
            
        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))