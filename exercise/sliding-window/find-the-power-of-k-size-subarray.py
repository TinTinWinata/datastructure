from typing import List
from collections import deque

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        arr = deque([nums[i] for i in range(k)])
        def check():
            nonlocal arr
            c_max = arr[0]
            for i in range(k - 1):
                c_max = max(arr[i+1], c_max)
                if arr[i] + 1 != arr[i + 1]:
                    return -1
            return c_max
        res = []
        nums.append(-1)
        for i in range(k, len(nums)):
            val = check()
            res.append(val)
            arr.popleft()
            arr.append(nums[i])
        return res

print(Solution().resultsArray([2,2,2,2,2], 4))
print(Solution().resultsArray([1,3,4], 2))