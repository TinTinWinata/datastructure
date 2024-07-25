from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i, v in enumerate(nums2):
            nums1[m + i] = v
        nums1.sort()
            
arr = [1,2,3,0,0,0]
Solution().merge(arr, 3, [2,5,6], 3)
print('arr : ',  arr)