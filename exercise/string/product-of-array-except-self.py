from collections import deque
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = deque()
        suffix = deque()
        n = len(nums)
        for i, v in enumerate(nums):
            vLast = nums[n - i - 1]
            if i == 0:
                prefix.append(v)
                suffix.appendleft(vLast)
            else:
                prefix.append(prefix[-1] * v)
                suffix.appendleft(suffix[0] * vLast)
        
        res = []
        for i, v in enumerate(nums):
            firstPrefix = 1
            if i - 1 >= 0:
                firstPrefix = prefix[i -1 ]
            lastSuffix = 1
            if i + 1 < n:
                lastSuffix = suffix[i + 1]
            res.append(firstPrefix * lastSuffix)
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
