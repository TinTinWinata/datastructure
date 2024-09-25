from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append([nums1[i], nums2[i]])
        arr.sort(key=lambda x: x[1], reverse=True)
        result = 0
        minheap = []
        temp_sum = 0
        for i, [a, b] in enumerate(arr):
            temp_sum += a
            heapq.heappush(minheap, a)
            if len(minheap) > k:
                popped = heapq.heappop(minheap)
                temp_sum -= popped
            if len(minheap) == k:
                print(temp_sum * b)
                result = max(result, temp_sum * b)
        return result
    
# print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))
# print(Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 1))