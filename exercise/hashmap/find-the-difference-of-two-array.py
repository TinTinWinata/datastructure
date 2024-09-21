from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp_set = set()
        same_set = set()
        for v in nums1:
            temp_set.add(v)
        for v in nums2:
            if v in temp_set:
                same_set.add(v)
        return [list(set([v for v in nums1 if v not in same_set])), list(set([v for v in nums2 if v not in same_set]))]

s = Solution()
# print(s.findDifference([1, 2, 3], [2, 4, 6]))
print(s.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))