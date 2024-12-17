from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(arr)
        for _ in range(k):
            _, i = heapq.heappop(arr)
            nums[i] = nums[i] * multiplier
            heapq.heappush(arr, (nums[i], i))
        return nums
    
print(Solution().getFinalState([2,1,3,5,6], 5, 2))