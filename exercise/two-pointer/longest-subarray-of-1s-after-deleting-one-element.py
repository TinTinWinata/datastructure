from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        result = 0
        k = 1
        for r, v in enumerate(nums):
            if v == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            else:
                result = max(result, r - l)
        return result

s = Solution()
# print(s.longestSubarray([1,1,0,1]))
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))