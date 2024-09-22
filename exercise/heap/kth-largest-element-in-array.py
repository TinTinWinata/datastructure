import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for v in nums[k:]:
            if v > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, v)
        return heap[0]
print(Solution().findKthLargest([3,2,1,5,6,4], 2))