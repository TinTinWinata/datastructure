from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        result = 0

        for r, v in enumerate(nums):
            if v == 0:
                k -= 1
            if k >= 0:
                result = max(result, r - l + 1)
            else:
                if nums[l] == 0:
                    k += 1
                l += 1
        return result

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))